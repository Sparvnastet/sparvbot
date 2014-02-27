import irc.client
import thread
import sys
import os
if 'gevent' in sys.modules:
    import zmq.green as zmq
else:
    import zmq

from . import utils


class SparvBot(irc.client.SimpleIRCClient):
    """Core IRC functionality"""

    def __init__(self, channel):
        super(SparvBot, self).__init__()

        # Handle service responses
        thread.start_new_thread(self.handle_outgoing, tuple())

        # Create publisher socket
        self.vent = utils.zmq_ctx.socket(zmq.PUB)
        self.vent.bind("inproc://dispatch")

        self.target = channel

    def service_add(self, service_class, *args, **kwargs):
        i = service_class(*args, **kwargs)
        i.start()

    def on_welcome(self, connection, event):
        """Join channel on connect"""
        if irc.client.is_channel(self.target):
            connection.join(self.target)

    def on_pubmsg(self, connection, event):
        """Event dispatcher"""
        cmd = event.arguments[0].split(" ", 1)
        if len(cmd) == 1:
            cmd.append(b'')

        self.vent.send_multipart((
            cmd[0].encode("utf8"), # Channel
            event.source.split("!")[0].encode("utf8"), # Username
            cmd[1].encode("utf8") # Payload
        ))

    def handle_outgoing(self):
        sink = utils.zmq_ctx.socket(zmq.PULL)
        sink.bind("inproc://bot")
        while True:
            msg = sink.recv()
            self.connection.privmsg(self.target, msg.decode("utf8"))

    def on_disconnect(self, connection, event):
        sys.exit(0)
