from flask_restful import Resource

from common.models import User, users_schema


class UserList(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

