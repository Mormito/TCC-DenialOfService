import os
import platform
import time

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def warning():
    clear()
    sign()
    print("> This code was built only for educacional purposes")
    time.sleep(1)
    print("> I am not responsible for any ilegal or non ethical uses ")
    print()
    time.sleep(2)
    clear()

def sign():
    BLUE = "\033[34m"
    RESET = "\033[0m"
    mogh = '''
 __  __                      _ _        
|  \/  | ___  _ __ _ __ ___ (_) |_ ___  
| |\/| |/ _ \| '__| '_ ` _ \| | __/ _ \ 
| |  | | (_) | |  | | | | | | | || (_) |
|_|  |_|\___/|_|  |_| |_| |_|_|\__\___/ 

    '''
    print(f"{BLUE}{mogh}{RESET}")


def results(target, port, number, type):
    GREEN = "\033[32m"
    RESET = "\033[0m"
    text = f'''
{GREEN}ATTACK SUCCESSFULLY EXECUTED{RESET}
+---------------------------------+
Target: {target}
Port: {port}
Number of Threads: {number}
Attack type: {type}
+---------------------------------+

'''
    print(text)
