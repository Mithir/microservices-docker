from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from settings import Settings

if __name__ == '__main__':

    print("Consumer is starting") 
    ##client = MongoClient('mongodb://mongoadmin:secret@mongo-on-docker:27017/?authSource=admin')
    client = MongoClient(f"mongodb://{Settings.MONGO_ADMIN}:{Settings.MONGO_SECRET}@{Settings.MONGO_HOST}:{Settings.MONGO_PORT}/?authSource=admin")
    print("After mongo client connection") 
    db=client.twitter
    consumer = KafkaConsumer(
        'hashtags',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        api_version=(0,11,5),
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=[f"{Settings.KAFKA_HOST}:{Settings.KAFKA_PORT}"])

    print("After kafka client connection") 

    for m in consumer:
        print(m.value) 
        try:
            db.hashtags.insert_many(m.value)

        except Exception as e:
            print(e)
