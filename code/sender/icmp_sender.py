from scapy.all import *

target_ip = "receiver"
icmp_request = IP(dst=target_ip, ttl=1) / ICMP()

send(icmp_request)
