import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("0.0.0.0", 8080))
clientsocket.send(b"hello")
