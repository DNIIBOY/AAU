from socket import *

HOST = ""
PORT = 9999
CONN_COUNTER = 0
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))

print("UDP server running...")
print(f"Listening for incoming connections in port {PORT}")

ILLEGAL_WORDS = [
    "tiananmen",
    "square",
    "fuck",
    "patrick",
    "xi",
    "jingping"
]


def censor(string):
    words = string.split()
    censored = []
    for word in words:
        if word.replace(",", "").casefold() in ILLEGAL_WORDS:
            censored.append("<nej>")
        else:
            censored.append(word)
    return " ".join(censored)


while True:
    CONN_COUNTER = CONN_COUNTER + 1
    r, a = s.recvfrom(BUFFER_SIZE)
    print(f"Connection {CONN_COUNTER} received from {a}")
    print(f"Incoming text: {r}")
    response = r.decode()
    response = censor(response).upper()
    s.sendto(response.encode(), a)
