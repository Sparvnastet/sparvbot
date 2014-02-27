from sparvbot import BaseService
from .models import Whitelist

class WhitelistService(BaseService):

    listen_channels = [
        "!wl",
    ]

    def __init__(self):
        super(WhitelistService, self).__init__()

    def help(self):
        self.send("Usage: !wl <username to add>")

    def handle_msg(self, chan, username, msg):
        try:
            entry = Whitelist.get(nick=username)
        except Whitelist.DoesNotExist:
            return self.send("You are not in the whitelist")

        if ' ' in msg or not msg:
            return self.help()

        entry = Whitelist.get_or_create(
            nick = msg
        )
        self.send("Nick '{0}' added".format(msg))
