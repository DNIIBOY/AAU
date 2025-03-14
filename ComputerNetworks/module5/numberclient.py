import socket
import random

HOST = "0.0.0.0"
PORT = 8888
BUFFER_SIZE = 4096

numbers = [random.random() * 100000000000 for _ in range(10000)]

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((HOST, PORT))
data = ",".join(map(str, numbers))
clientsocket.send(data.encode())
response = clientsocket.recv(BUFFER_SIZE)
clientsocket.close()

values = list(map(float, response.decode().split(",")))
print(values)
