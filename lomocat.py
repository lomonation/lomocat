import argparse, subprocess
from twitter import *

class LomoCat(object):
    def __init__(self):
        self.twitter = Twitter()

    def tweet(self, message):
        print self.twitter.post(message)

    def minecraft(self, command):
        if (command.lower() == 'start'):
            print 'Starting server.'
            subprocess.call(['screen', '-S', 'minecraft', '-X', 'stuff', 'java -Xmx1024M -Xms1024M -jar minecraft_server.1.7.5.jar nogui\015'])
        elif (command.lower() == 'stop'):
            print 'Stopping server.'
            subprocess.call(['screen', '-S', 'minecraft', '-X', 'stuff', 'stop\015'])
        else:
            print 'Command not recognized.'

if __name__ == '__main__':
    cat = LomoCat()

    parser = argparse.ArgumentParser(description='a bot for Lomonation')

    parser.add_argument('-t', '--tweet', metavar='message', type=str, help='post a tweet')

    parser.add_argument('--minecraft', metavar='command', type=str, help='issue a Minecraft server command')

    args = parser.parse_args()

    if (args.tweet is not None):
        cat.tweet(args.tweet)

    if (args.minecraft is not None):
        cat.minecraft(args.minecraft)