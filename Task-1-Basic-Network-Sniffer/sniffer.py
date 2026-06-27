from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    print("=" * 60)

    if packet.haslayer(IP):
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")
        print(f"Protocol       : {packet[IP].proto}")

    print(f"Packet Summary : {packet.summary()}")

print("Basic Network Sniffer Started...")
print("Capturing 10 packets...\n")

sniff(prn=packet_callback, count=10)

print("\nPacket Capture Completed Successfully!")