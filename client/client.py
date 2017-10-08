import socket
import os
import email

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input('Masukkan IP host :')
port = 3000
client_socket.connect((host, port))
location = "/home/frieda/PycharmProjects/5115100063_5115100071/progjar-tugas1/client/downloads"
os.chdir(location)
location = os.getcwd()

reqfile = raw_input('Input nama file yang ingin didownload :')

client_socket.send(reqfile)
unduh, file = reqfile.split()
with open(file, 'wb') as file_to_write:
    count = 0
    while(True):
        data = client_socket.recv(1024)
        for char in data:
            if count >= 2:
                file_to_write.write(char)
            if char == '\n':
                count+=1
        if not data:
            break
file_to_write.close()
print client_socket.recv(1024)
client_socket.close()