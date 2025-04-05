import ollama
from flask import render_template, request
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


@bp.route("/", methods=["GET", "POST"])
def demo():
    form = DemoForm(request.form)
    if request.method == "GET":
        return render_template("demo.html", form=form)
    else:
        response: ChatResponse = ollama.chat(
            model=form.models.data,
            messages=[
                {
                    "role": "user",
                    "content": form.prompt.data,
                },
            ],
        )
        return render_template("demo.html", form=form, response=response.message.content)
