import socket
import struct

message = b"Where is the printer?"
multicast_group = ("224.1.1.1", 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.2)

ttl = struct.pack("b", 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
try:
    # Send data to the multicast group
    print(f"Sending {message} to {multicast_group}")
    sent = sock.sendto(message, multicast_group)
    # Look for responses from all recipients
    while True:
        print("waiting to receive")
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print("timed out, no more responses")
            break
        else:
            print(f"received {data} from {server}")
finally:
    print("closing socket")
    sock.close()
