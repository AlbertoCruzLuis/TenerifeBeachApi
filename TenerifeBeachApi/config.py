class Config(object):
    DEBUG = False
    SECRET_KEY = "secretkey"
    USERNAME = "admin"
    PASSWORD = "adminjwt"
    MONGO_URI = 'mongodb://localhost/TenerifeBeachDB'

class DevelopmentConfig(Config):
    DEBUG = True
