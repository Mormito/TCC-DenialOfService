from base import *

def control():
    warning()

    opcao = int(input('''
 CONTROL PANEL !
_________________
                                         
1 - ICMP REQUEST
2 - HTTP REQUEST
_________________
                                           
Digite o numero que representa o que quer fazer: ''').strip())
    
    if(opcao == 1):
        sendICMP()
    elif(opcao == 2):
        requestHTTP()

control()
    