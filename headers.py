import requests
import pyfiglet 
import colorama
from colorama import Fore
colorama.init() 

ascii_banner = pyfiglet.figlet_format("Headers")
print(Fore.CYAN + ascii_banner)
print("-" * 50)

url = input("Enter URL: ")
# if url is does not have https then this will automaticlly add it
if not url.startswith("https"):
    url = "https://" + url
#sends a head request 
response = requests.head(url)
#if the request is successful or not. prints out header information
print(Fore.GREEN + f'Status Code: {response.status_code}')   #HTTP CODE 
for header in response.headers:
    print(Fore.YELLOW + f'{header}: {response.headers[header]}')
    
    
    
    #official name HyberHeader
