import sys
from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        proto_name = "Unknown"
        if proto == 1:
            proto_name = "ICMP"
        elif proto == 6:
            proto_name = "TCP"
        elif proto == 17:
            proto_name = "UDP"

        print("\n" + "="*50)
        print(f"[+] New Packet: {src_ip} -> {dst_ip} | Protocol: {proto_name}")

        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"    [Layer 4] TCP Port: {src_port} -> {dst_port}")
            
            if packet[TCP].payload:
                payload_data = bytes(packet[TCP].payload)
                print(f"    [Payload] (First 100 bytes): {payload_data[:100]}")

       
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"    [Layer 4] UDP Port: {src_port} -> {dst_port}")
            
            if packet[UDP].payload:
                payload_data = bytes(packet[UDP].payload)
                print(f"    [Payload] (First 100 bytes): {payload_data[:100]}")

    
        elif packet.haslayer(ICMP):
            print(f"    [Layer 4] ICMP Type: {packet[ICMP].type} | Code: {packet[ICMP].code}")

def main():
    print("[*] Starting Basic Network Sniffer...")
    print("[*] Listening for network traffic... (Press Ctrl+C to stop)")
    
    try:
        sniff(prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\n[*] Stopping the sniffer. Goodbye!")
        sys.exit(0)
    except PermissionError:
        print("\n[!] Error: Access Denied. Please run this script with Administrator/Root privileges.")
        sys.exit(1)

if __name__ == "__main__":
    main()