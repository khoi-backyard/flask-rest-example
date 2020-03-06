from flask import Flask, Blueprint
from flask_restful import Api, Resource

from resources.v1.user import UserList

v1_bp = Blueprint('v1', __name__)
v1_api = Api(v1_bp)

v1_api.add_resource(UserList, '/users')
