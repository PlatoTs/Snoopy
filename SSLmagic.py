import pyfiglet
import colorama
import sys
import ssl
import socket
import os 
from urllib.parse import urlparse
from colorama import Fore
colorama.init()
os.system('cls' if os.name == 'nt' else 'clear')
#Art Banner 
art = pyfiglet.figlet_format("WhereSSL")
print(Fore.CYAN + art)
print("-" * 50)
#target
hostname = input("Enter IP or URL: ")
#establish ssl connection 
context = ssl.create_default_context()
#default port 443 HTTPS and establish encrypted SSL connection
with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert() # Where certificate is stored // f-strings makes it more readable
        if cert and ('subjectAltName' in cert or 'subject' in cert):
            print(Fore.CYAN + f"The certificate is valid for {cert['subjectAltName']}") 
            print(Fore.CYAN + f"Valid from: {cert['notBefore']}")
            print(Fore.CYAN + f"Valid until: {cert['notAfter']}")
            url = urlparse(f"https://{hostname}")
            if url.scheme == "https":
                print(Fore.GREEN + "The website is using HTTPS")
            else:
                print(Fore.RED + "The website is not using HTTPS")
            print(f"Issued by: {cert['issuer']}")
            print(f"Serial number: {cert['serialNumber']}")
        else:
            print("The website's certificate is invalid or not found") 
