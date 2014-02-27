#!/bin/sh
export IRC_CHANNEL="#sparvtestet"
export IRC_SERVER="irc.freenode.org"
export IRC_PORT="6667"
export IRC_BOT_NAME="sparvbot"

export TWITTER_OAUTH_TOKEN=""
export TWITTER_OAUTH_SECRET=""
export TWITTER_CONSUMER_KEY=""
export TWITTER_CONSUMER_SECRET=""

export DB_FILE="database.db"

./sparven.py
