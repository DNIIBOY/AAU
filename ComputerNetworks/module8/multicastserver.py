import socket
import struct

multicast_group = "224.1.1.1"
server_address = ("0.0.0.0", 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack("4sL", group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print("\nwaiting to receive message")
    data, address = sock.recvfrom(1024)
    print("received %s bytes from %s" % (len(data), address))
    print(data)
    print("sending acknowledgement to", address)
    sock.sendto(b"ack", address)
