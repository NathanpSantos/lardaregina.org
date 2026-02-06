from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .public import public_bp
    from .system import system_bp

    app.register_blueprint(public_bp)                 # /
    app.register_blueprint(system_bp, url_prefix="/sistema")

    return app
