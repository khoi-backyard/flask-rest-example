from flask import Flask, Blueprint
from flask_restful import Api, Resource

v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)

class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

v1_api.add_resource(TodoItem, '/todos/<int:id>')

