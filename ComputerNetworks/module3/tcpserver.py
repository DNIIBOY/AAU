from socket import *

HOST = ""
PORT = 8888
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

c, a = s.accept()
print("Connection")
c.settimeout(0.5)

with open("hej.jpg", "wb") as f:
    while True:
        try:
            bytes_read = c.recv(BUFFER_SIZE)
        except TimeoutError:
            print("done")
            break
        f.write(bytes_read)

print("File received and saved as hej.jpg")
c.send(f"Hi there! Got your file from {a[0]}".encode())
c.close()
