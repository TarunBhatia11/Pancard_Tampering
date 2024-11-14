import os
from os import environ


class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'tarunbhatia@123'

    UPLOADS = "Pan+Card+Tampering+Flask+App/Pan Card Tampering Flask App/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFUAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugConfig(Config):
    DEBUG = True

