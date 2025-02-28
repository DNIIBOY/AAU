from socket import *

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect((SERVER_IP, SERVER_PORT))

with open("sejt.jpg", "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # File transmission is complete
            break
        s.sendall(bytes_read)

print("File sent successfully.")

# Wait for server response
data = s.recv(BUFFER_SIZE)
print(f"Received data: {data.decode()}")

s.close()
