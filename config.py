import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}" \
        .format(DB_USER="khoi", DB_PASS="",
                DB_ADDR="127.0.0.1",
                DB_NAME="bluebox")


class ProductionConfig(BaseConfig):
    DEBUG = False
