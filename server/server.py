import socket
import os
import select
import threading
import Queue

host = socket.gethostname()
port = 3000
print host
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host,port))
serversocket.listen(10)
os.chdir('/home/frieda/PycharmProjects/5115100063_5115100071/progjar-tugas1/server/dataset')
location = os.getcwd()

open_client = []
message_to_send = []
print location

q = Queue.Queue()

class SenderThread(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.file = file
    def run(self):
        print file
        current_socket.send("client-id: klien-" + repr(q.get()))
        current_socket.send("\n")
        current_socket.send("file-size:" + repr(len(file)))
        current_socket.send("\n")
        with open(file, 'rb') as file_to_send:
            for content in file_to_send:
                current_socket.send(content)

while(True):
    try:
        rlist, wlist, xlist = select.select([serversocket] + open_client, open_client, [])
        for current_socket in rlist:  # sockets that can be read
            if current_socket is serversocket:  # if there is a new client
                (new_socket, address) = serversocket.accept()
                open_client.append(new_socket)  # clients list
                id = len(open_client)
                q.put(id)
            else:
                data = current_socket.recv(1024)
                print data
                unduh, file = data.split()
                if len(data) == 0:
                   open_client.remove(current_socket)  # remove user if he quit.
                else:
                    if os.path.isfile(file):
                        t=SenderThread(file)
                        t.run()
                open_client.remove(current_socket)
    except KeyboardInterrupt:
        serversocket.close()