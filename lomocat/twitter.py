import tweepy
from config import *
from listener import Listener

class Twitter(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.stream = tweepy.streaming.Stream(auth, Listener())
        self.stream.filter(follow=ADMIN, track=['#lomocat'])

    def post(self, message):
        if (len(message) < 141):
            self.api.update_status(message)
            return 'Tweet posted!'
        else:
            return 'Tweet not posted: message too long!'