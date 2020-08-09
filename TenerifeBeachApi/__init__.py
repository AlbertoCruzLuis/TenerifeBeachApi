from flask_cors import CORS
from .app import app
from .api import api_bp
from .main import main
from .commands import create_data

def create_app():
    CORS(app)
    app.register_blueprint(api_bp)
    app.register_blueprint(main)

    app.cli.add_command(create_data)

    return app

