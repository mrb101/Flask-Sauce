import os


base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[sauce]'
    FLASK_MAIL_SENDER = 'Sauce Admin <admin@suace.com>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    dev_db = os.environ.get('DEV_DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = dev_db
    print SQLALCHEMY_DATABASE_URI

class TestingConfig(Config):
    TESTING = True
    test_db = os.environ.get('TEST_DATABASE_URL')
    SQL_ALCHEMY_DATABASE_URI = test_db


class ProductionConfig(Config):
    db = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = db


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
