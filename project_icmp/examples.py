#send.py

from scapy.all import *

# Create an IP packet with a fragment offset of 100
ip = IP(dst="192.168.1.1", id=12345, frag=100)/ICMP()

# Create an ICMP packet with a type of 3 (destination unreachable) and code of 4 (fragmentation needed and DF set)
icmp = IP(dst="192.168.1.1")/ICMP(type=3, code=4)/ip

# Send the packet
send(icmp)

#rcv.py


import socket
import struct

try:
    # create a raw socket listening for ICMP packets
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    while True:
        packet, address = sock.recvfrom(65535)
        icmp_header = packet[20:28]
        icmp_type, code, checksum, packet_id, seq = struct.unpack('bbHHh', icmp_header)
        print(f'Received ICMP packet: type={icmp_type}, code={code}, packet_id={packet_id}, seq={seq}')
except OSError as e:
    print(f'Error: {e}')
