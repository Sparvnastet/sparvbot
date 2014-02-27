#!/usr/bin/env python
from sparvbot import SparvBot
import os

from services.tweet import TweetService
from services.whitelist import WhitelistService

if __name__ == "__main__":
    bot = SparvBot(os.getenv("IRC_CHANNEL"))
    bot.connect(
        os.getenv("IRC_SERVER"),
        int(os.getenv("IRC_PORT")),
        os.getenv("IRC_BOT_NAME")
    )

    bot.service_add(TweetService,
                    os.getenv("TWITTER_OAUTH_TOKEN"),
                    os.getenv("TWITTER_OAUTH_SECRET"),
                    os.getenv("TWITTER_CONSUMER_KEY"),
                    os.getenv("TWITTER_CONSUMER_SECRET"))

    bot.service_add(WhitelistService)

    bot.start()

    pass
