from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)
    app.secret_key = "demo key. replace later."

    # import all blueprints (there shouldn't be too many)
    from app.example import bp as example_bp
    from app.houyi_test import bp as houyi_bp

    # register them
    app.register_blueprint(example_bp)
    app.register_blueprint(houyi_bp)

    # root that just redirects to my example
    @app.route("/")
    def home():
        return redirect(url_for("example.demo"))

    return app
