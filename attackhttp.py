import requests
import threading
from concurrent.futures import ThreadPoolExecutor

def request(destiny, destiny_port):
    try:
        r = requests.get(f"http://{destiny}:{destiny_port}")
        rr = r.status_code
        print(rr)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar a {destiny}:{destiny_port} == {e}")

def request_flood(destiny, destiny_port, num_of_packets, num_of_workers):
    with ThreadPoolExecutor(max_workers=num_of_workers) as executor:
        for _ in range(num_of_packets):
            executor.submit(request, destiny, destiny_port)
        
    print(f"Total de pacotes enviados: {num_of_packets}")



request_flood("google.com", 80, 50, 10)