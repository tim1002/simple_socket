# server.py
# a simple socket-server application

import socket, time

# create a socket object
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine address
host = socket.gethostname()
port = 9999

# bind created socked to address host/port
ss.bind((host, port))

# queue up to 5 requests
ss.listen(5)

while 1:
    # establish connection
    cs, addr = ss.accept()
    print('got a connection from %s ' % str(addr))
    currentTime = time.ctime(time.time()) + '\r\n'
    cs.send(currentTime.encode('ascii'))
    cs.close()
