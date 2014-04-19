import tweepy

class Listener(tweepy.StreamListener):
	def on_status(self, status):
		print "%d: %s" % (status.user.screen_name, status.text)

	def on_error(self, error):
		print "Error"
		return True