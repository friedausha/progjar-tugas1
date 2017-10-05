import socket
import os
import sys
import cgi

host = 'localhost'
port = 3000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host,port))
serversocket.listen(10)
os.chdir('/home/frieda/PycharmProjects/5115100063_5115100071/server/dataset')
location = os.getcwd()
print location
while(True):
    clientsocket, address = serversocket.accept()
    data = clientsocket.recv(1024)
    unduh, file = data.split()
    print file
    if os.path.isfile(file):
        print file
        with open(file, 'rb') as file_to_send:
            for content in file_to_send:
                clientsocket.send(content)
    else:
        clientsocket.send("File tidak ditemukan")
    clientsocket.close()
serversocket.close()