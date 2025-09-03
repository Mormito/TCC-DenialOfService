from scapy.all import IP, TCP, Raw, sr1, RandShort, RandIP, send

destiny = "8.8.8.8"
destiny_port = 443

HTTP_REQUEST = (
    b"GET / HTTP/1.1\r\n"
    b"Host: " + destiny.encode() + b"\r\n"
    b"User-Agent: Scapy-Client/1.0\r\n"
    b"Connection: close\r\n"
    b"\r\n"
)

default_seq = 1000

syn_ip_packet = IP(dst=destiny)
syn_tcp_packet = TCP(sport=23456, dport=destiny_port, flags="S", seq=default_seq)

syn_packet = syn_ip_packet / syn_tcp_packet

syn_response = sr1(syn_packet, verbose=False, timeout=2) #synack
source_port = syn_response[TCP].dport

if syn_response and syn_response[TCP].flags == "SA":

    ack_ip_packet = IP(dst=destiny)
    ack_tcp_packet = TCP(sport=syn_packet[TCP].sport, dport=destiny_port, flags="A", seq=syn_response[TCP].ack, ack=syn_response[TCP].seq+1 )
    ack_packet = ack_ip_packet / ack_tcp_packet
    send(ack_packet, verbose=False)

    print(f"\nSYN Seq: {syn_packet[TCP].seq}")
    print(f"SYN Ack: {syn_packet[TCP].ack}")
    print(f"SYN Source Port: {syn_packet[TCP].sport}")
    print(f"SYN Destiny Port: {syn_packet[TCP].dport}")

    print(f"\nSYN-ACK Seq: {syn_response[TCP].seq}")
    print(f"SYN-ACK Ack: {syn_response[TCP].ack}")
    print(f"SYN-ACK Source Port: {syn_response[TCP].sport}")
    print(f"SYN-ACK Destiny Port: {syn_response[TCP].dport}")

    print(f"\nACK Seq: {ack_packet[TCP].seq}")
    print(f"ACK Ack: {ack_packet[TCP].ack}")
    print(f"ACK Source Port: {ack_packet[TCP].sport}")
    print(f"ACK Destiny Port: {ack_packet[TCP].dport}")


