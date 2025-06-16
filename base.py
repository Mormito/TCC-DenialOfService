from scapy.all import *
from scapy.all import IP, ICMP

import requests
import threading

from utils import *

import time

#send é para enviar
#dst é destino
#ICMP é pacote, tipo um ping

# Uma requisição ICMP é uma mensagem de tipo 8 do protocolo Internet Control Message Protocol (ICMP).
def sendICMP(): #Essa função serve para enviar requisições ICMP 
    time.sleep(0.2)
    alvo = "" #input("Escreva a url ou o IP do alvo: ").strip()
    qtde = 300 #int(input("Quantidade de pacotes enviados: ").strip())

    clear()
    print(f"Alvo: {alvo}")
    print(f"Quantidade de pacotes: {qtde}")

    try:
        pacotes = [IP(dst=alvo)/ICMP() for _ in range(qtde)]
        send(pacotes)
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def pingAlvo(url):
    try:
        resposta = requests.get(url)
        print(f"Ping em {url}: {resposta.status_code}")
    except requests.RequestException as e:
        print(f"Erro no ping | {url}: {e}")

def requestHTTP():
    alvo = "https://" + "" #input("Escreva a url do alvo: ").strip()
    qtde = 5 #int(input("Quantidade de pacotes enviados: ").strip())

    clear()
    print(f"Alvo: {alvo}")
    print(f"Quantidade de requisições: {qtde}")
    print()

    threads = []

    for _ in range(qtde):
        thread = threading.Thread(target=pingAlvo, args=(alvo,)) #Aqui ele define um thread como o método PING e de args seu alvo!
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join








def warning():
    clear()
    sign()
    print("> Esse código tem apenas fins educacionais, não me responsabilizo por má conduta ou uso deste programa.")
    time.sleep(1)
    print("> Nesse código viso aprender envio de requisições/dados para um IP, qualquer uso antiético é de sua responsabilidade!")
    print()
    time.sleep(1)
    clear()
