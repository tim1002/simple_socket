# client.py
# a simple client socket

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine address
host = socket.gethostname()
port = 9999

# connect to hostname on the port
s.connect((host, port))

# receive no more than 1024 bytes
tm = s.recv(1024)
# close connection
s.close()

print('time got from the server is %s ' % tm.decode('ascii'))
