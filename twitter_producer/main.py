from twitter_client import TwitterProvider
from twitter_client import TwitterStreamListener
from handlers import HashtagHandler
from settings import Settings
import time
from datetime import datetime

if __name__ == '__main__':

    try:    
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        keywords = Settings.KEYWORDS
        hashtag_handler = HashtagHandler()
        stream_listener = TwitterStreamListener(hashtag_handler)
        provider = TwitterProvider(keywords, stream_listener)
        provider.start()
        print("finished...sleeping before terminating")
        time.sleep(10000000)
    except Exception as e:
        print(e)
        print("failed...sleeping before terminating")
        time.sleep(10000000)
