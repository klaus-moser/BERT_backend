from flask import Blueprint
from flask_restful import Resource, reqparse
from models.process import ProcessModel

main = Blueprint('main', __name__)


class Process(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'text',
        type=str,
        required=False,
        help='This field is for the text.'
    )

    @classmethod
    def post(cls):
        """
        Receive a text to classify.
        """
        data = cls.parser.parse_args()
        if data:
            m = ProcessModel()
            m.text = data['text']
            ret = m.process()
            return ret, 200
        else:
            return {"message": "Empty text."}, 200
