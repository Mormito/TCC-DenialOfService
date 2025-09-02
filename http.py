from scapy.all import IP, TCP, Raw, sr1, RandShort, RandIP

#def send_http_packet(destiny, destiny_port):

destiny = "google.com" 
## Como este código ainda não ataca, utilizei sites comuns para enviar requisições HTTP, apenas para testar se estava enviando a requisição.
## Em nenhum momento causando danos, lentidões ou interrupções a sites.
destiny_port = 80 ##

HTTP_REQUEST = (
    b"GET / HTTP/1.1\r\n"
    b"Host: " + destiny.encode() + b"\r\n"
    b"User-Agent: Scapy-Client/1.0\r\n"
    b"Connection: close\r\n"
    b"\r\n"
)

#PACOTE SYN COMPLETO (ip,tcp,juncao)
syn_ip_packet = IP(dst=destiny)
syn_tcp_packet = TCP(sport=RandShort(), dport=destiny_port, flags="S", seq=1000)
syn_complete_packet = syn_ip_packet / syn_tcp_packet

syn_ack_response = sr1(syn_complete_packet, verbose=False, timeout=2)
print(f"\nSYN-ACK response | {syn_ack_response}")

if syn_ack_response and syn_ack_response[TCP].flags == "SA":

    #numero de sequencia retornado pelo servidor 
    my_ack_seq = syn_ack_response[TCP].ack
    print(f"ACK SEQ: {my_ack_seq}")
    my_ack_ack = syn_ack_response[TCP].seq + 1
    print(f"ACK ACK: {my_ack_ack}")

    #PACOTE ACK COMPLETO (ip,tcp,juncao)
    ack_source_port = syn_ack_response[TCP].dport
    ack_destiny_port = syn_ack_response[TCP].sport
    ack_ip_packet = IP(dst=syn_ack_response[IP].src)
    ack_tcp_packet = TCP(sport=ack_source_port, dport=ack_destiny_port, flags="A", seq=my_ack_seq, ack=my_ack_ack)

    ack_complete_packet = ack_ip_packet / ack_tcp_packet

    ack_response = sr1(ack_complete_packet, verbose=False)

    print(f"""
        Pacote ACK
        Sequencia: {my_ack_seq}
        Seq ACK: {my_ack_ack}
        Porta de origem: {ack_source_port}
        Porta de destino: {ack_destiny_port}    
    """)

    #numero de sequencia retornado pelo servidor 
    my_http_seq = my_ack_seq
    my_http_ack = my_ack_ack

    #PACOTE HTTP COMPLETO (ip,tcp,juncao)
    http_source_port = syn_ack_response[TCP].dport
    print(http_source_port)
    http_destiny_port = syn_ack_response[TCP].sport
    http_ip_packet = IP(dst=ack_response[IP].src)
    http_tcp_packet = TCP(sport=http_source_port, dport=http_destiny_port, flags="PA", seq=my_http_seq, ack=my_http_ack)

    http_complete_packet = http_ip_packet / http_tcp_packet / Raw(load=HTTP_REQUEST)

    http_response = sr1(http_complete_packet, verbose=False, timeout=3)

    if http_response and http_response.haslayer(Raw):
        print("\n--- Website content: ---\n")
        print(http_response[Raw].load.decode(errors='ignore'))
        print("\n--- END ---\n")
    else: 
        print("HTTP Failed")
        print(f"Server response | {http_response}")

else: print("No response received.")


#simplesmente estou enlouquecendo tentando fazer isso, mas vai dar certo.