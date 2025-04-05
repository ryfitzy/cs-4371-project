from flask import Blueprint

bp = Blueprint("example", __name__, url_prefix="/example")

from app.example import example
