from sparvbot import BaseService
import twitter

from .whitelist.models import Whitelist


class TweetService(BaseService):

    listen_channels = [
        "!tweet"
    ]

    def __init__(self, oauth_token, oauth_secret,
                 consumer_key, consumer_secret):

        super(TweetService, self).__init__()

        self.tweeter = twitter.Twitter(
            auth=twitter.OAuth(
                oauth_token,
                oauth_secret,
                consumer_key,
                consumer_secret
            )
        )

    def handle_msg(self, chan, username, msg):
        try:
            entry = Whitelist.get(nick=username)
        except Whitelist.DoesNotExist:
            return self.send("You are not in the whitelist")

        self.send("Tweeting '{0}'".format(msg))

        try:
            self.tweeter.statuses.update(
                status=msg
            )
        except twitter.TwitterError as e:
            self.send(": ".join((
                "Error",
                str(e).split("\n")[-1]
            )))
        except Exception as e:
            self.send("An unhandled error occured")
