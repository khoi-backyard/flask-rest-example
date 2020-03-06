from http import HTTPStatus

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from common.models import User, users_schema, user_schema, db


class UserResource(Resource):
    def get(self, id):
        user = User.query.get_or_404(id)
        return user_schema.dump(user)


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        user_dict = request.get_json()
        try:
            user = user_schema.load(user_dict)
            db.session.add(user)
            db.session.commit()
            return user_schema.dump(user)
        except ValidationError as err:
            return err.messages, HTTPStatus.BAD_REQUEST
