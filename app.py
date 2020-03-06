from flask import Flask
from common.models import db
from flask_migrate import Migrate
from resources.v1 import v1_bp

def create_app(config_object):
    app = Flask(__name__)

    app.config.from_object(config_object)
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(v1_bp, url_prefix='/v1')

    return app


app = create_app('config.DevelopmentConfig')
