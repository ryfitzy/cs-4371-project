from flask import Blueprint

bp = Blueprint("houyi_test", __name__, url_prefix="/houyi_test")

from app.houyi_test import houyi