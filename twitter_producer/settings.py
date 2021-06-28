from os import environ

class Settings:
    KEYWORDS = environ.get('keywords') or 'love'
    TWITTER_APP_KEY = environ.get('twitter_app_key') 
    TWITTER_APP_SECRET = environ.get('twitter_app_secret') 
    TWITTER_KEY = environ.get('twitter_key') 
    TWITTER_SECRET = environ.get('twitter_secret') 
    KAFKA_HOST = environ.get('kafka_host') or 'kafka'
    KAFKA_PORT = environ.get('kafka_port') or '9093'