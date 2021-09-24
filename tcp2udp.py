import socket

TCP_host = '127.0.0.1'
TCP_port = 55551

UDP_host = '127.0.0.1'
UDP_port = 55552

sentences = ['RSA','THS','VDM','VTG']

def filter(data):
    if data[3:6].decode() in sentences:
        UDP.sendto(data, (UDP_host, UDP_port))
        print(data)

TCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
TCP.bind((TCP_host,TCP_port))
TCP.listen(1)
connection,address = TCP.accept()

UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data = connection.recv(1024)
    filter(data)
