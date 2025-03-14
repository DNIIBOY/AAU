import threading
import socket


HOST = ""
PORT = 8888
BUFFER_SIZE = 4096


class ClientThread(threading.Thread):
    def __init__(self, clientsocket):
        super().__init__()
        self.csocket = clientsocket

    def run(self) -> None:
        data = self.csocket.recv(BUFFER_SIZE)
        message = data.decode()
        numbers = list(map(float, message.replace(" ", "").split(",")))
        self.csocket.send(",".join(map(str, sorted(numbers))).encode())


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

while True:
    server.listen(1)
    clientsock, _ = server.accept()
    newthread = ClientThread(clientsock)
    newthread.start()
