from socket import gethostbyname
from os import system

print("\033[1;33m*[Welcome to IP-OSINT! ]*")
print("")
target = input("\033[1;32mEnter the host: \033[1;37m")
targetIP = gethostbyname(target)
print(f"\033[1;31m-Target IP ===>', \033[1;37m{targetIP}")
print("")
system("bash main.sh")
