from scapy.all import *

print(sniff(filter="icmp", count=1, prn=lambda p: p.show()))
