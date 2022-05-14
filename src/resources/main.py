from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/', methods=["GET"])
def index():
    """
    Index Resource/landing page.
    """
    return "Hello World", 200
