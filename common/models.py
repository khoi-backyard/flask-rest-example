from flask_marshmallow import Marshmallow, Schema
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from marshmallow import fields

db = SQLAlchemy()
ma = Marshmallow()

class TimestampMixin(object):
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

class User(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    locations = db.relationship('Location', backref='user', lazy=True)

    def __init__(self, email):
        self.email = email

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Location(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, latitude, longitude, date, user_id):
        self.latitude = latitude
        self.longitude = longitude
        self.date = date
        self.user_id = user_id

