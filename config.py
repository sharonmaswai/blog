import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sharon-maswai:qwerty@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS= False

    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_PORT=os.environ.get('MAIL_PORT')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG=True
config_options={
    'development':DevConfig,
    'production':ProdConfig
}    