#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import os
import zmq
import time

port = os.environ['ZMQ_BIND_PORT']
sock = "tcp://0.0.0.0:" + port

print("Creating Context")
context = zmq.Context()
print("Creating socket")
socket = context.socket(zmq.PAIR)
print("Binding to " + sock)
socket.bind(sock)

while True:
    print("Waiting for message", flush=True)
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
