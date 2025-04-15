import ollama
from flask import redirect, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField
from app.prompt_injections import ATTACKS
from . import bp

model_histories = {}  # In-memory chat history

class ChatForm(FlaskForm):
    models = SelectField(
        "Select model:",
        choices=[("mistral", "Mistral"), ("gemma3", "Gemma 3"), ("llama3.2", "LLaMA 3.2")],
    )
    attacks = SelectField(
        "Prompt Injection:",
        choices=[
            ("", "None"),
            ("leakage", "Prompt Leakage"),
            ("manipulation", "Content Manipulation"),
            ("info_gathering", "Information Gathering"),
            ("spam", "Spam Generation"),
        ],
    )

@bp.route("/", defaults={"selected_model": "mistral"}, methods=["GET", "POST"])
@bp.route("/<selected_model>", methods=["GET", "POST"])
def index(selected_model):
    form = ChatForm()
    form.models.data = selected_model

    model_histories.setdefault(selected_model, [])
    history = model_histories[selected_model]

    if request.method == "POST":
        if "attacks" in request.form:
            attack_type = form.attacks.data or request.form.get("attacks")
            if attack_type in ATTACKS:
                user_input = ATTACKS[attack_type]["harness"]
                history.append({"role": "user", "content": user_input})

                response = ollama.chat(model=selected_model, messages=history)
                if response.message:
                    history.append({"role": "assistant", "content": response.message.content})

        return redirect(url_for("chat.index", selected_model=selected_model))

    return render_template("chat.html", form=form, history=model_histories, selected_model=selected_model)


@bp.route("/reset/<model>", methods=["POST"])
def reset_chat(model):
    model_histories[model] = []  # Clear history
    return redirect(url_for("chat.index", selected_model=model))
