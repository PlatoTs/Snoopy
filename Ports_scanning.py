import pyfiglet
import sys
import socket
import threading
import colorama
import os
from datetime import datetime
from colorama import Fore
colorama.init()
os.system('cls' if os.name == 'nt' else 'clear')
#Art banner
art = pyfiglet.figlet_format("Stalkin-Ports")
print(Fore.CYAN + art)

# Defining a target
target = input(str("Enter IP address or URL: "))

# Add Banner of beginning of scan
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
# creating socket with type/ timeout 5 sec / attempts for connections /0 = SUCCESSFUL 
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)
    result = s.connect_ex((target,port))
    if result == 0:
            print(Fore.GREEN +"Port {} is open".format(port))
    s.close()
#runs this function first before scan_port
try:
    # Get IP address from URL.
    ip = socket.gethostbyname(target)
    print(Fore.MAGENTA + "IP address:", ip)

    # scan ports from 1 to 1000. Faster scanning threading
    for port in range(1, 1000):
        threading.Thread(target=scan_port, args=(port,)).start()
# If server is unreachable or wrong input these errors will be displayed.
except socket.error:
    print(Fore.RED + "Error: Unknown hostname/IP.")
    sys.exit()
