from flask import Flask
from common.models import db
from flask_migrate import Migrate

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    migrate = Migrate(app, db)
    return app


app = create_app('config.DevelopmentConfig')
