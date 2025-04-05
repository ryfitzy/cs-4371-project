import ollama
from flask import Response, render_template, request, stream_with_context
from flask_wtf import FlaskForm
from ollama import ChatResponse
from wtforms import SelectField, SubmitField, TextAreaField

from . import bp


class DemoForm(FlaskForm):
    prompt = TextAreaField("Enter prompt here")
    submit = SubmitField("Submit")
    models = SelectField(
        "Select model:",
        choices=[("mistral", "Mistral"), ("gemma3", "Gemma 3"), ("llama3.2", "Llama 3.2")],
    )


@bp.route("/")
def demo():
    form = DemoForm()
    return render_template("demo.html", form=form)


@bp.route("/stream", methods=["POST"])
def streamed_response():
    model = request.form.get("models")
    prompt = request.form.get("prompt")

    if not (model and prompt):
        return "Unknown error"

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        stream=True,
    )

    def generate():
        for chunk in response:
            message = chunk.message.content
            if message:
                yield message

    return stream_with_context(generate())
