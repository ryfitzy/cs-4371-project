import ollama
from flask import redirect, url_for, render_template, request, session, jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField

from . import bp

class ChatForm(FlaskForm):
    prompt = TextAreaField("Your message:")
    submit = SubmitField("Send")
    models = SelectField(
        "Select model:",
        choices=[
            ("mistral", "Mistral"),
            ("gemma3", "Gemma 3"),
            ("llama3.2", "LLaMA 3.2")
        ]
    )

@bp.route("/", methods=["GET", "POST"])
def index():
    form = ChatForm()
    if 'history' not in session:
        session['history'] = {}

    if request.method == "POST" and form.validate_on_submit():
        model = form.models.data
        user_input = form.prompt.data

        # Initialize model conversation history
        session['history'].setdefault(model, [])
        history = session['history'][model]

        history.append({"role": "user", "content": user_input})

        response = ollama.chat(model=model, messages=history)

        if response.message:
            history.append({"role": "assistant", "content": response.message.content})

        session.modified = True  # Important to save session changes

    return render_template("chat.html", form=form, history=session.get('history', {}))

@bp.route("/reset/<model>", methods=["POST"])
def reset_chat(model):
    if 'history' in session and model in session['history']:
        session['history'][model] = []
        session.modified = True
    return redirect(url_for("chat.index"))