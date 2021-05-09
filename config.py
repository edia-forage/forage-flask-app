import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-know-anything'
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')

    # Simply connect to Cloud SQL Proxy sidecar @ 127.0.0.1:5432
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@127.0.0.1:5432/{DB_NAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
