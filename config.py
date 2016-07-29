import os


base_dir = os.path.abspath(os.path.dirname(__file__))

class config:
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
    dev_sqlite = 'sqlite:///' + os.path.join(base_dir, 'data-dev.sqlite')
    SQL_ALCHEMY_DATABASE_URI = dev_db or dev_sqlite


class TestingConfig(Config):
    TESTING = True
    test_db = os.environ.get('TEST_DATABASE_URL')
    test_sqlite = 'sqlite:///' + os.path.join(base_dir, 'data-test.sqlite')
    SQL_ALCHEMY_DATABASE_URI = test_db or test_sqlite


class ProductionConfig(Config):
    db = os.environ.get('DATABASE_URL')
    sqlite = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
    SQL_ALCHEMY_DATABASE_URI = db or sqlite


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
