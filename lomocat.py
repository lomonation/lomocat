import argparse
from twitter import *

class LomoCat(object):
    def __init__(self):
        self.twitter = Twitter()

    def tweet(self, message):
        print self.twitter.post(message)

if __name__ == '__main__':
    cat = LomoCat()

    parser = argparse.ArgumentParser(description='DESCRIPTION')

    parser.add_argument('-t', '--tweet', metavar='message', type=str, help='post a tweet')

    args = parser.parse_args()

    if ('tweet' in args):
        cat.tweet(args.tweet)