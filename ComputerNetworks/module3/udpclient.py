from socket import *

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
BUFFER_SIZE = 1024
HOST = ""
PORT = 9998

DESTINATION = (SERVER_IP, SERVER_PORT)
ADDRESS = (HOST, PORT)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(ADDRESS)
s.sendto(b"Hej Xi Jingping, jeg hedder Patrick, fuck dig.", DESTINATION)
print("Data sent.")
r, a = s.recvfrom(BUFFER_SIZE)
print(f"Received data: {r}")
