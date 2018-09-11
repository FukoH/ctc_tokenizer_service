import os




class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DICT_PATH = 'ctc_dict.txt'
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    #TODO 数据库地址
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vocabulary.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'oracle://bi_ui:bi_ui@172.19.37.14:1521/gis'


class ProductionConfig(Config):
    #TODO 生产环境
    SQLALCHEMY_DATABASE_URI = 'oracle://bi_ui:bi_ui@172.19.37.14:1521/gis'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
