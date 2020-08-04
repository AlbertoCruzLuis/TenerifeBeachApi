from flask_cors import CORS
from .app import app
from .api import api_bp
from .main import main

def create_app():
    CORS(app)
    app.register_blueprint(api_bp)
    app.register_blueprint(main)

    return app

