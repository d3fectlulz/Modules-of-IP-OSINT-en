import socket
from os import system


system("setterm -foreground green")
print("User")
system("whoami")
print("\n")
print("State")
system("hostname")
print("\n")
print("IP Machine")
system("hostname -i")
print("\n")
print("Public Ip")
system("curl ifconfig.me")
print("\n")
print("")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Private IP")
print(s.getsockname()[0])
print("\n")
print("Version ssh")
system("ssh -V")

print("")
system("bash main.sh")
