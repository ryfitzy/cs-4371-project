from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def example():
        return __name__

    return app
