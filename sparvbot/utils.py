import sys
if 'gevent' in sys.modules:
    import zmq.green as zmq
else:
    import zmq
zmq_ctx = zmq.Context()
