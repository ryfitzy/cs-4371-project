import importlib
import json

from flask import Response, redirect, render_template, request, stream_with_context, url_for
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
            ("ethical_violation", "Ethical Violation"),
        ],
    )


@bp.route("/", defaults={"selected_model": "mistral"}, methods=["GET", "POST"])
@bp.route("/<selected_model>", methods=["GET", "POST"])
def index(selected_model):
    form = ChatForm()
    form.models.data = selected_model

    model_histories.setdefault(selected_model, [])

    return render_template("chat.html", form=form, history=model_histories, selected_model=selected_model)


@bp.route("/stream_attack")
def stream_attack():
    selected_model = request.args.get("model")
    attack_type = request.args.get("attack_type")

    def generate():
        try:
            module_path = f"app.prompt_injections.{attack_type}"
            attack_module = importlib.import_module(module_path)

            history: list[dict[str, str | bool]] = []

            for update in attack_module.run_attack(selected_model):
                for role in ["user", "assistant", "system"]:
                    if role in update:
                        history.append({"role": role, "content": update[role]})

                yield f"data: {json.dumps(update)}\n\n"

            model_histories[selected_model] = history

        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return Response(stream_with_context(generate()), mimetype="text/event-stream")


@bp.route("/reset/<model>", methods=["POST"])
def reset_chat(model):
    model_histories[model] = []
    return redirect(url_for("chat.index", selected_model=model))
