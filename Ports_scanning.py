import pyfiglet
import sys
import socket
import threading
import colorama
from datetime import datetime
from colorama import Fore
colorama.init()

ascii_banner = pyfiglet.figlet_format("Stalkin-Ports")
print(ascii_banner)

# Defining a target
target = input(str("Enter IP address or URL: "))

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

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

    # scan ports from 1 to 65535 
    for port in range(1, 65535):
        threading.Thread(target=scan_port, args=(port,)).start()
# If server is unreachable these errors will be displayed.
except socket.error:
    print(Fore.RED + "Error: Server is offline.")
    sys.exit() 
except socket.gaierror:
    print(Fore.RED + "Error:Unknown hostname/IP.")
    sys.exit()
