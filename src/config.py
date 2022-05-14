from os import environ


modes: dict = {'PRODUCTION': 'ProductionConfig',
               'DEVELOP': 'DevelopmentConfig',
               'TEST': 'TestingConfig'}


class Config(object):
    """
    Default configuration.
    """
    ADMIN: int = 1
    ENV = 'production'
    DEBUG = False
    TESTING = False
    FLASK_SERVER_NAME = 'localhost:5000'
    FLASK_THREADED = True
    PROPAGATE_EXCEPTIONS = True


class ProductionConfig(Config):
    """
    Production configuration.
    """
    pass


class DevelopmentConfig(Config):
    """
    Development configuration.
    """
    ENV = 'development'
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class TestingConfig(Config):
    """
    Testing configuration.
    """
    ENV = 'testing'
    TESTING = True
    LOG_LEVEL = 'DEBUG'
