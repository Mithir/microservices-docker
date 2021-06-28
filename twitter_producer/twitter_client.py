from tweepy import Stream
from tweepy import API
from tweepy import OAuthHandler
from settings import Settings
from tweepy import StreamListener, RateLimitError
from threading import Thread


class TwitterProvider:
    """
    a wrapper to the tweepy client library
    responsible of the actual connection to twitter and wiring the events
    """
    def __init__(self, keywords, stream_listener):
        self._keywords = keywords
        self._stream_listener = stream_listener  # twitterStreamListener.TwitterStreamListener()

    def start(self):
        retries = 1
        stream = self.get_stream()
        while retries < 5:
            try:
                if not stream.running:
                    stream.filter(track=[self._keywords], is_async=True)
            except RateLimitError:
                print("Rate limit error... not restarting")
                raise
            except Exception as e:
                print("Error. Restarting Stream.... Error: ")
                print(e.__doc__)
                print(e)
                retries += 1
        print("finished retries")

    def get_stream(self):
        auth = OAuthHandler(Settings.TWITTER_APP_KEY, Settings.TWITTER_APP_SECRET)
        auth.set_access_token(Settings.TWITTER_KEY, Settings.TWITTER_SECRET)
        api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

        return Stream(auth=api.auth, listener=self._stream_listener)


class TwitterStreamListener(StreamListener):
    """
    handling the events wired by the twitter provider
    """
    def __init__(self, hashtag_handler):
        super().__init__(api=None)
        self._hashtagHandler = hashtag_handler

    def on_status(self, status):
        thread = Thread(target=self._hashtagHandler.handle, args=[status])  # consider moving the new thread to the handler
        thread.start()

    def on_error(self, status_code):
        # if the error for bad credentials, end stream
        print("Got status code %d" % status_code)
        if status_code == 401:
            return False

        # rate limit, close
        if status_code == 420:
            return False

        if status_code == 406:
            return False
