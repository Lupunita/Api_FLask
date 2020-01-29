import os

class Config(object):


    DB_HOST = os.environ.get('DB_HOST', default='localhost')
    DB_NAME = os.environ.get('DB_NAME', default='testovacka')
    DB_USER = os.environ.get('DB_USERNAME', default='flask')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', default='')
    DB_PORT = os.environ.get('DB_PORT', default='5432')
    SECRET_KEY = os.environ.get('SECRET_KEY')


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"