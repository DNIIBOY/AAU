import sqlite3
import socket
import json

DB_NAME = "store.db"
con = sqlite3.connect(DB_NAME)
cur = con.cursor()

p = cur.executescript("""
    DROP TABLE IF EXISTS Items;
    CREATE TABLE Items(Name TEXT, Price INT);
    """)

HOST = ""
PORT = 8888
BUFFER_SIZE = 1024


class ClientThing:
    def __init__(self, clientsocket):
        super().__init__()
        self.csocket = clientsocket
        self.con = sqlite3.connect(DB_NAME)
        self.cur = self.con.cursor()

    def run(self):
        data = self.csocket.recv(BUFFER_SIZE)
        message = data.decode()
        data = json.loads(message)
        if "action" not in data:
            self.csocket.send(b"400")
            self.csocket.close()
            return

        self.handle_action(data["action"], data)
        self.csocket.close()

    def handle_action(self, action: str, data: dict) -> None:
        match action:
            case "add":
                print(self.cur.execute(f"INSERT INTO Items VALUES({data['name']}, {data['price']})"))
                self.csocket.send(b"200")
            case "get":
                output = []
                items = self.cur.execute("SELECT * FROM Items")
                for item in enumerate(items):
                    output.append({"id": item[0], "name": item[1], "price": item[2]})
                self.csocket.send(json.dumps(output).encode())
            case "remove":
                try:
                    item = self.cur.execute("SELECT * FROM Items WHERE ID = ?", (data["id"],)).fetchone()
                    self.cur.execute("DELETE FROM Items WHERE ID = ?", (data["id"],))

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
    ClientThing(clientsock).run()
