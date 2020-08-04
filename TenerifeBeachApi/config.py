class Config(object):
    DEBUG = False
    MONGO_URI = 'mongodb://localhost/TenerifeBeachDB'

class DevelopmentConfig(Config):
    DEBUG = True
