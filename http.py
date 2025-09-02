from scapy.all import IP, TCP, Raw, sr1, RandShort, RandIP

#def send_http_packet(destiny, destiny_port):

destiny = "hitt.com.br" ##
destiny_port = 80 ##

HTTP_REQUEST = (
    b"GET / HTTP/1.1\r\n"
    b"Host: " + destiny.encode() + b"\r\n"
    b"User-Agent: Scapy-Client/1.0\r\n"
    b"Connection: close\r\n"
    b"\r\n"
)

ip_packet = IP(dst=destiny)
syn_packet = TCP(sport=RandShort(), dport=destiny_port, flags="S", seq=1000)
complete_packet = ip_packet / syn_packet

syn_ack_response = sr1(complete_packet, verbose=False, timeout=2)
print()
print(f"SYN-ACK response | {syn_ack_response}")

if syn_ack_response and syn_ack_response[TCP].flags == "SA":
    print(f"Correct")
else: print("No response received")


#numero de sequencia retornado pelo servidor 
my_seq = syn_ack_response[TCP].ack
my_ack = syn_ack_response[TCP].seq + 1
ack_source_port = syn_ack_response[TCP].dport
ack_destiny_port = syn_ack_response[TCP].sport
ip_ack_packet = IP(dst=syn_ack_response[IP].src)


print(f"""
      
    Pacote ACK
    Sequencia: {my_seq}
    Seq ACK: {my_ack}
    Porta de origem: {ack_source_port}
    Porta de destino: {ack_destiny_port}    

""")

ack_packet = TCP(sport=ack_source_port, dport=ack_destiny_port, flags="A", seq=my_seq, ack=my_ack)
complete_ack_packet = ip_ack_packet / ack_packet
ack_response = sr1(complete_ack_packet, verbose=False, timeout=2)

#if ack_response