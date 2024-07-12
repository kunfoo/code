#!/usr/bin/env python3
from scapy.all import IP, TCP, sr

ip_packet = IP(dst="10.1.2.3")
tcp_packet = TCP(flags="SP", dport=(443))
print(sr(ip_packet / tcp_packet))
