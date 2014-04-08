import argparse, subprocess
from twitter import *
from personality import *

class LomoCat(object):
    def __init__(self):
        self.twitter = Twitter()

    def tweet(self, message):
        print self.twitter.post(message)

    def mc_command(self, command):
        return subprocess.call(['screen', '-S', 'minecraft', '-X', 'stuff', '%s\015' % command])

    def minecraft(self, command):
        if (command.lower() == 'start'):
            print 'Starting server.'
            self.mc_command('java -Xmx1024M -Xms1024M -jar minecraft_server.1.7.5.jar nogui')
        elif (command.lower() == 'stop'):
            print 'Stopping server.'
            self.mc_command('stop')
        else:
            print 'Command not recognized.'

    def broadcast(self, message):
        pass
        # subprocess.call([])

    def cartograph(self, command):
        if (command.lower() == 'map'):
            print 'Rendering map.'
        elif (command.lower() == 'signs'):
            print 'Rendering signs.'
        else:
            print 'Command not recognized.'

def main():
    cat = LomoCat()

    parser = argparse.ArgumentParser(description='a bot for Lomonation')

    parser.add_argument('-t', '--tweet', metavar='message', type=str, help='post a tweet')

    parser.add_argument('-m', '--minecraft', metavar='command', type=str, help='issue a Minecraft server command')

    parser.add_argument('-b', '--broadcast', metavar='message', type=str, help='broadcast a global server message')

    parser.add_argument('-c', '--cartograph', metavar='command', type=str, help='render server map')

    args = parser.parse_args()

    if (args.tweet is not None):
        cat.tweet(args.tweet)

    if (args.minecraft is not None):
        cat.minecraft(args.minecraft)

    if (args.broadcast is not None):
        cat.broadcast(args.broadcast)

    if (args.cartograph is not None):
        cat.cartograph(args.cartograph)

if __name__ == '__main__':
    main()