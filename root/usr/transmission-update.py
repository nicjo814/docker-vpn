#!/usr/bin/python
import socket
import sys

var_filename = '/etc/socket-variables.txt'

def getVarFromFile(filename):
    import imp
    f = open(filename)
    global var_data
    var_data = imp.load_source('var_data', '', f)
    f.close()

getVarFromFile(var_filename)
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((var_data.host, var_data.port))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    received = sock.recv(1024)
    print "Sent:     {}".format(data)
    print "Received: {}".format(received)
except socket.error:
    print "Failed to connect to Transmission"
finally:
    sock.close()
