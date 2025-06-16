import os
import platform

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


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