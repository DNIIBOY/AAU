import threading
import socket
from dataclasses import dataclass
import json


@dataclass
class SalesItem:
    name: str
    price: float

    def json(self) -> dict:
        return {"name": self.name, "price": self.price}


ITEMS = []
ITEM_LOCK = threading.Lock()


HOST = ""
PORT = 8888
BUFFER_SIZE = 1024


class ClientThread(threading.Thread):
    def __init__(self, clientsocket):
        super().__init__()
        self.csocket = clientsocket

    def run(self):
        data = self.csocket.recv(BUFFER_SIZE)
        message = data.decode()
        data = json.loads(message)
        if "action" not in data:
            self.csocket.send(b"400")
            self.csocket.close()
            return

        with ITEM_LOCK:
            self.handle_action(data["action"], data)
        self.csocket.close()

    def handle_action(self, action: str, data: dict) -> None:
        match action:
            case "add":
                ITEMS.append(SalesItem(data["name"], data["price"]))
                self.csocket.send(b"200")
            case "get":
                output = []
                for i, item in enumerate(ITEMS):
                    output.append({"id": i, "name": item.name, "price": item.price})
                self.csocket.send(json.dumps(output).encode())
            case "remove":
                try:
                    item = ITEMS.pop(data["id"])
                    self.csocket.send(json.dumps(item.json()).encode())
                except IndexError:
                    self.csocket.send(b"404")
            case _:
                self.csocket.send(b"400")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

while True:
    server.listen(1)
    clientsock, _ = server.accept()
    newthread = ClientThread(clientsock)
    newthread.start()
