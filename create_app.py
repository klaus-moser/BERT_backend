from flask import Flask, render_template
from flask_restful import Api

from src.resources.process import Process
from src.config import modes


def create_app(mode: str = 'DEPLOY') -> Flask:
    """
    Creates a Flask app with a specific configuration (Default: PRODUCTION.)
    :param mode: 'PRODUCTION', 'DEVELOP', 'TEST'
    :return: Flask app.
    """
    app = Flask(__name__)

    # Check mode
    if mode not in modes:
        mode = 'DEPLOY'

    # Load config
    app.config.from_object("config." + modes[mode])
    app.app_context().push()
    api = Api(app=app)

    @app.errorhandler(404)
    def page_not_found(error) -> tuple:
        return render_template('error/error-404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(error) -> tuple:
        return render_template('error/error-500.html'), 500

    # Endpoints
    api.add_resource(Process, '/process')

    return app
