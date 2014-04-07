import tweepy
from config import *

class Twitter(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def post(self, message):
        if (len(message) < 141):
            self.api.update_status(message)
            return 'Tweet posted!'
        else:
            return 'Tweet too long.'