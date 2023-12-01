#!/usr/bin/python3

import socket

# This by default will listen on port 8080. Feel free to change this to whatever port you need.

host = socket.gethostname()
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(2)
print('Server is listening for incoming connections')

while True:
    conn,addr = server.accept()
    print("Connection Received from %s" % str(addr))
    msg = 'Connection Established'+ "\r\n"
    conn.send(msg.encode('ascii'))
    conn.close()
