from scapy.all import IP, TCP, Raw, send, sr1, RandShort
import threading


destiny = "127.0.0.1"
destiny_port = 80

HTTP_REQUEST = (
    b"GET / HTTP/1.1\r\n"
    b"Host: " + destiny.encode() + b"\r\n"    # O 'Host' é importante para servidores virtuais
    b"User-Agent: Scapy HTTP Client\r\n"      # Identificação do cliente
    b"Connection: close\r\n"                  # Fechar a conexão após a resposta
    b"\r\n"                                   # Linha vazia final para encerrar o cabeçalho
)

ip_packet = IP(dst=destiny)
syn_packet = TCP(sport=RandShort(), dport=destiny_port, flags="S", seq=1000)

complete_packet = ip_packet / syn_packet

syn_ack_response = sr1(syn_packet, verbose=False, timeout=2, iface="wlp0s20f3")

if syn_ack_response and syn_ack_response.haslayer(TCP) and syn_ack_response[TCP].flags == "SA":
    print("SYN-ACK recebido! Conexão estabelecida.")

    #incomplete...