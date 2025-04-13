from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)
    app.secret_key = "demo key. replace later."

    # import all blueprints (there shouldn't be too many)
    # from app.example import bp as example_bp
    from app.chat import bp as chat_bp

    # register them
    app.register_blueprint(chat_bp)

    @app.route("/")
    def home():
        return redirect(url_for("chat.index"))

    return app
