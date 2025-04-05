from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField

from . import bp


class DemoForm(FlaskForm):
    prompt = TextAreaField("Enter prompt here")
    submit = SubmitField("Submit")


@bp.route("/", methods=["GET", "POST"])
def demo():
    form = DemoForm(request.form)
    if request.method == "GET":
        return render_template("demo.html", form=form)

    return render_template("demo.html", form=form)
