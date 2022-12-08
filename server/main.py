import ast
import socket
from threading import Thread

ip = "0.0.0.0"
in_port = 8080
buffer_size = 512

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server.bind((ip, in_port))



def process(data):
    try:
        data_dict = ast.literal_eval(data)
    except: return

    if (len(data_dict) == 0): return

    if (len(data_dict) > 1):
        file = open(data_dict['dir'], "wb")
        file.write(data_dict['data'].encode('utf-8'))
        file.close()
    
    file = open(data_dict['dir'], "rb")
    text = ""
    for i in file.readlines():
        text += i.decode('utf-8')
    file.close()
    return text


def main():
    while True:
        data = server.recvfrom(buffer_size)
        server.sendto(process(data[0]), data[1])
        

Thread(target=main).start()
