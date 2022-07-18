import argparse
import threading
from node import MyNode

parser = argparse.ArgumentParser(description='Process nodes')
parser.add_argument('--id', type=int)
args = parser.parse_args()._get_kwargs()

def main():
    rendezvous = ('192.168.1.101', 55555)
    node = MyNode(rendezvous,args[0][1])

    listener = threading.Thread(target=node.listen, daemon=True)
    listener.start()

    while 1:
        inp = input("> ")
        try:
            msg = {
                "from" :{
                    "ip" : node.ip,
                    "port" : node.port,
                },
                "to" :{
                    "ip" : node.dip,
                    "port" : node.dport,
                },
                "message": inp
                }
            node.sendMessage(str(msg))
        except:
            print("Im have no parent")
            node.sendMessage()

main()