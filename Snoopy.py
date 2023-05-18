import os
import colorama
from colorama import *
import pyfiglet

colorama.init()

#clears the terminal 
os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to Snoopy".center(50, "-"))

name = pyfiglet.figlet_format("Snoopy", font = "slant")
print(Fore.RED + name)

#Attack Options
print("List of Recon:")
print("-" * 50)
print("[1].Ports scanner ")
print("[2].SSL Finder ")
print("[3].Crawler ")
print("[4].Headers ")


#Imports scripts for each method.
selection = input("Input number: ")
if selection == "1":
	import Ports_scanning
elif selection == "2":
	import SSLmagic
elif selection == "3":
	import crawk
elif selection == "4":
	import HyperHeaders
else:
	print("Invalid Selection. Please enter from 1-4.")

