import threading
import socket
from dataclasses import dataclass
from random import randint

HOST = ""
PORT = 8888
BUFFER_SIZE = 1024


@dataclass
class Message:
    client_id: int
    message: str

MESSAGES = []


class ClientThread(threading.Thread):
    def __init__(self, clientsocket):
        super().__init__()
        self.csocket = clientsocket
        self.csocket.settimeout(0.5)
        self.client_id = randint(0, 65535)

    def run(self):
        while self.csocket:
            data = self.csocket.recv(BUFFER_SIZE)
            message = data.decode()

        r = self.csocket.recv(BUFFER_SIZE)
        self.csocket.send(b"test")
        self.csocket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
while True:
    server.listen(1)
    clientsock, _ = server.accept()
    newthread = ClientThread(clientsock)
    newthread.start()
