import ollama
from flask import redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextAreaField

from . import bp


class ChatForm(FlaskForm):
    prompt = TextAreaField("Your message:")
    submit = SubmitField("Send")
    models = SelectField(
        "Select model:",
        choices=[
            ("mistral", "Mistral"),
            ("gemma3", "Gemma 3"),
            ("llama3.2", "LLaMA 3.2"),
            ("deepseek-r1", "DeepSeek-R1"),
        ],
    )


@bp.route("/", defaults={"selected_model": "mistral"}, methods=["GET", "POST"])
@bp.route("/<selected_model>", methods=["GET", "POST"])
def index(selected_model):
    form = ChatForm()
    form.models.data = selected_model

    if "history" not in session:
        session["history"] = {}

    if request.method == "POST" and form.validate_on_submit():
        user_input = form.prompt.data
        session["history"].setdefault(selected_model, [])
        history = session["history"][selected_model]

        history.append({"role": "user", "content": user_input})

        response = ollama.chat(model=selected_model, messages=history)
        if response.message:
            history.append({"role": "assistant", "content": response.message.content})

        session.modified = True

        return redirect(url_for("chat.index", selected_model=selected_model))

    return render_template("chat.html", form=form, history=session.get("history", {}), selected_model=selected_model)


@bp.route("/reset/<model>", methods=["POST"])
def reset_chat(model):
    if "history" in session and model in session["history"]:
        session["history"][model] = []
        session.modified = True
    return redirect(url_for("chat.index", selected_model=model))
