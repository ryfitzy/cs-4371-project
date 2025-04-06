from flask import Blueprint

bp = Blueprint("example", __name__, url_prefix="/example")

from app.example import example  # this is needed for the main app to be able to locate example.demo
