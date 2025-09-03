from scapy.all import IP, TCP, Raw, sr1, RandShort, RandIP, send

destiny = "10.0.2.5"
destiny_port = 8080

http_request = (
    b"GET / HTTP/1.1\r\n"
    b"Host: " + destiny.encode() + b"\r\n"
    b"User-Agent: Scapy-Client/1.0\r\n"
    b"Connection: close\r\n"
    b"\r\n"
)

default_seq = 1000

syn_ip_packet = IP(dst=destiny)
syn_tcp_packet = TCP(sport=RandShort(), dport=destiny_port, flags="S", seq=default_seq)

syn_packet = syn_ip_packet / syn_tcp_packet

syn_response = sr1(syn_packet, verbose=False, timeout=2) #synack
print(f"\nSYN PACKET SUCEFULLY SENT | FLAG == {syn_packet[TCP].flags}")
source_port = syn_response[TCP].dport


if syn_response and syn_response[TCP].flags == "SA":
    print(f"SYN-ACK SUCEFULLY RECEIVED | FLAG == {syn_response[TCP].flags}")

    http_ip_packet = IP(dst=destiny)
    http_tcp_packet = TCP(sport=source_port, dport=destiny_port, flags="A", seq=syn_response[TCP].ack, ack=syn_response[TCP].seq+1)
    http_packet = http_ip_packet / http_tcp_packet / http_request

    final_response = sr1(http_packet, verbose=False, timeout=10)
    
    if final_response: print(f"ACK PACKET SUCEFFULY SENT | FLAG == {http_packet[TCP].flags}")

    if final_response[TCP].flags == "R":
        print(
            f"\nSeq and ack (SYN-ACK): {syn_response[TCP].seq} | {syn_response[TCP].ack}"
            f"\nSeq and ack (HTTP-PACKET): {http_packet[TCP].seq} | {http_packet[TCP].ack}"
            f"\nSeq and ack: {final_response[TCP].seq} | {final_response[TCP].ack}"
            f"\nFlags: {final_response[TCP].flags}"
        )

    if Raw in final_response:
        print("\n--- Server Response ---\n")
        print(final_response[Raw].load.decode())
    else:
        print("\nNo raw data in the response. Received flags:", final_response[TCP].flags)


