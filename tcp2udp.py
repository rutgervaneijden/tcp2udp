# 2021 Rutger van Eijden

import socket

TCP_port = 55551
UDP_address = '127.0.0.1'
UDP_port = 55552

TCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCP.bind(('',TCP_port))

UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

TCP.listen(1)
connection,address = TCP.accept()

while True:
    data = connection.recv(1024)
    UDP.sendto(data, (UDP_address, UDP_port))
    print(data)    