import socket
import sys
from os import system


print("\033[1;32m ____            _     ____  ____")
print("\033[1;32m|  _ \ ___  _ __| |_  |___ \|___ \ ")
print("\033[1;32m| |_) / _ \| '__| __|   __) | __) |")
print("\033[1;32m|  __/ (_) | |  | |_   / __/ / __/")
print("\033[1;32m|_|   \___/|_|   \__| |_____|_____|")
print("\n")
system("setterm -foreground green")
ip = input("[+]Enter the IP you want to scan > \033[1;37m")
print("")

ip_addr = (ip)
portList = [22]

for port in portList:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))                             
        if status == 0:
            print("\033[1;33mPort | Service | State")
            print("")                     
            print(f"\033[1;Port: \033[1;32m{port} SSH - Open")
        else:
            print("\033[1;33mPort | Service | State")
            print("")
            print(f"\033[1;31mPort: \033[1;32m{port} SSH - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        sys.exit()

print("")
system("bash main.sh")
