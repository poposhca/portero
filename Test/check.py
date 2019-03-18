import socket
import sys
# Create a TCP socket
address = '192.168.86.32'
port = 20010
s = socket.socket()
print "Attempting to connect to %s on port %s" % (address, port)
try:
    s.connect((address, port))
    print "Connected to %s on port %s" % (address, port)
    print True
except socket.error, e:
    print "Connection to %s on port %s failed: %s" % (address, port, e)
    print False
finally:
    s.close()