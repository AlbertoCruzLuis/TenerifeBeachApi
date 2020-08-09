import os
import secrets

class Config(object):
    DEBUG = False
    SECRET_KEY = secrets.token_hex(16)

class DevelopmentConfig(Config):
    DEBUG = True
    USERNAME = "admin"
    PASSWORD = "adminjwt"
    MONGO_URI = 'mongodb://localhost/TenerifeBeachDB'
    URL = "http://localhost:5000/"

class ProductionConfig(Config):
    DEBUG = False
    USERNAME =  os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')
    MONGO_URI = os.environ.get('MONGO_URI')
    URL = "https://tenerifebeachapi.herokuapp.com/"