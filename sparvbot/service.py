import threading
import sys
if 'gevent' in sys.modules:
    import zmq.green as zmq
else:
    import zmq
from .utils import zmq_ctx
from . import utils


class BaseService(threading.Thread):

    listen_channels = []

    def __init__(self):
        super(BaseService, self).__init__()
        self.daemon = True

        self._sink = zmq_ctx.socket(zmq.SUB)
        self._sink.connect("inproc://dispatch")
        for c in self.listen_channels:
            self._sink.setsockopt(zmq.SUBSCRIBE, c)

        self._vent = zmq_ctx.socket(zmq.PUSH)
        self._vent.connect("inproc://bot")

    def send(self, msg):
        self._vent.send(msg)

    def handle_msg(self, chan, msg):
        raise NotImplementedError("You need to implement a handle_msg method")

    def run(self):
        while True:
            chan, username, msg = self._sink.recv_multipart()
            self.handle_msg(chan, username, msg)
