from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto= packet[IP].proto
        print(f"Packet: {src} -> {dst} | Protocol: {proto}")

        print("Starting Network Sniffer...")
sniff(prn=packet_callback, count=10)
