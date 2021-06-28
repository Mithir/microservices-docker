from os import environ

class Settings:
    KAFKA_HOST = environ.get('kafka_host') or 'kafka'
    KAFKA_PORT = environ.get('kafka_port') or '9093'
    MONGO_PORT = environ.get('mongo_port') or '27017'
    MONGO_HOST = environ.get('mongo_host') or 'mongo-on-docker'
    MONGO_ADMIN = environ.get('mongo_admin') or 'mongoadmin'
    MONGO_SECRET = environ.get('mongo_secret') or 'secret'