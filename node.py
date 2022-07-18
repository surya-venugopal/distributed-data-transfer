from asyncio import sleep
import socket


class MyNode:
    def __init__(self,rendezvous,id):
        self.ip, self.port = ("0.0.0.0",40000 + id)
        print('connecting to rendezvous server')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))
        self.sock.sendto(b'0', rendezvous)

        while True:
            data = self.sock.recv(1024).decode()

            if data.strip() == 'ready':
                print('checked in with server, waiting')
                break

        data = self.sock.recv(1024).decode()
        print(data)
        if(data == "Im root"):
            pass
        else:
            data = data.split(' ')
            print(data)
            self.dip, self.dport = data[0],int(data[1])
            
            print('\ngot parent')
            print('parent ip:          {}'.format(self.dip))
            print('parent port:        {}'.format(self.dport))
            # print('  dest port:   {}\n'.format(self.dport))

    def listen(self):
        while True:
            data = self.sock.recv(1024)
            print('\rpeer: {}\n> '.format(data.decode()), end='')

    def sendMessage(self,msg=""):
        if(msg!=""):
            self.sock.sendto(msg.encode(), (self.dip, self.dport))

        
