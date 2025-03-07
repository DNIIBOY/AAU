import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

s.send(b"Hello, server!")
data = s.recv(BUFFER_SIZE)
print(f"Received data: {data.decode()}")
