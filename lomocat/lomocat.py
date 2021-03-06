import argparse, subprocess
from config import SERVER_IP, SERVER_PORT
from twitter import *
from server import Status, COMMAND_LIST
from personality import *

class LomoCat(object):
    def __init__(self):
        self.twitter = Twitter()

    def tweet(self, message):
        print self.twitter.post(message)

    def status(self):
        result = subprocess.Popen(['nmap', SERVER_IP, '-p', SERVER_PORT], stdout=subprocess.PIPE).communicate()[0]

        if ('open') in result:
            status = Status.online
        elif ('closed' in result):
            status = Status.offline
        else:
            status = Status.none

        return status

    def mc_command(self, command):
        return subprocess.call(['screen', '-S', 'minecraft', '-X', 'stuff', '%s\015' % command])

    def minecraft(self, command):
        if (command[0].lower() == 'start'):
            if (self.status() == Status.online):
                print 'Server already running.'
            else:
                print 'Starting server.'
                self.mc_command('java -Xmx1024M -Xms1024M -jar minecraft_server.1.7.5.jar nogui')
        elif (command[0].lower() == 'stop'):
            if (self.status() == Status.offline or self.status() == Status.none):
                print 'No server instance found.'
            else:
                print 'Stopping server.'
                self.mc_command('stop')
        elif (command[0] in COMMAND_LIST):
            if (self.status() == Status.online):
                print 'Executing: /%s' % ' '.join(command) 
                self.mc_command(' '.join(command))
            else:
                print 'Could not execute command. Server not online.'
        else:
            print 'Command not recognized: %s' % command[0]

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

    parser.add_argument('-s', '--status', action='store_true', help='check server status')

    parser.add_argument('-t', '--tweet', metavar='<message>', type=str, help='post a tweet')

    parser.add_argument('-m', '--minecraft', metavar='<command>', type=str, nargs='+', help='issue a Minecraft server command')

    parser.add_argument('-c', '--cartograph', metavar='[map|signs]', type=str, help='render server map')

    args = parser.parse_args()

    if (args.status):
        print cat.status().name.capitalize()

    if (args.tweet is not None):
        cat.tweet(args.tweet)

    if (args.minecraft is not None):
        cat.minecraft(args.minecraft)

    if (args.cartograph is not None):
        cat.cartograph(args.cartograph)

# if __name__ == '__main__':
#     main()