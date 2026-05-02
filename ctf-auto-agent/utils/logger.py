from colorama import Fore, init
init(autoreset=True)

def info(msg):
    print(Fore.CYAN + "[INFO] " + msg)

def success(msg):
    print(Fore.GREEN + "[SUCCESS] " + msg)

def warn(msg):
    print(Fore.YELLOW + "[WARN] " + msg)

def error(msg):
    print(Fore.RED + "[ERROR] " + msg)
