from kafka import KafkaProducer
from json import dumps
from settings import Settings

class HashtagHandler:
    """
    The listener should call this handler with new statuses.
    when handling a new status it will extract the hashtags and publish to kafka
    """
    def __init__(self):
        print("started initializing producer")
        self.producer = KafkaProducer(
            value_serializer=lambda m: dumps(m).encode('utf-8'), 
            api_version=(0,11,5),
            bootstrap_servers=[f'{Settings.KAFKA_HOST}:{Settings.KAFKA_PORT}'])
        print("FINISHED initializing producer")

    def handle(self, status):
        if hasattr(status, 'retweeted_status'):  # not interested in retweets
            return

        hashtag_metadatas = status.entities.get('hashtags')
        if len(hashtag_metadatas) == 0:  # only interested in tweets with hashtags
            return

        print("Sending hashtags")
        print(hashtag_metadatas)
        self.producer.send("hashtags", hashtag_metadatas)
        print("finished Sending hashtags")


