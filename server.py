from math import ceil
from pydoc import cli
import socket

known_port = 50002

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.1.101', 55555))

while True:
    clients = []

    while True:
        try:
            data, address = sock.recvfrom(128)

            print('connection from: {}'.format(address))
            if(address not in clients):
                clients.append(address)

            sock.sendto(b'ready', address)
            i = len(clients)-1
            i = ceil(i/2) - 1
            if(i==-1):
                sock.sendto("Im root".encode(), address)
            else:
                sock.sendto('{} {}'.format(clients[i][0], clients[i][1]).encode(), address)
        except:
            pass