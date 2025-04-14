from flask import Blueprint

bp = Blueprint("chat", __name__, url_prefix="/chat")

from app.chat import chat  # this is needed for the main app to be able to locate example.demo
