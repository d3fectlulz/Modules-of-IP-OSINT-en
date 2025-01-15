import socket
import sys
from os import system

print("\033[1;32m ____")
print("\033[1;32m/ ___|  ___ __ _ _ __  _ __   ___ _ __")
print("\033[1;32m\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|")
print("\033[1;32m ___) | (_| (_| | | | | | | |  __/ |")
print("\033[1;32m|____/ \___\__,_|_| |_|_| |_|\___|_|")
print("\n")
system("setterm -foreground green")
ip = input("[+]Enter the IP you want to scan > \033[1;37m")
print("")

ip_addr = (ip)
port1ftp = [21]
port2ssh = [22]
port3telnet = [23]
port4smb = [139]
port5netbiosns = [137]
port6microsoftds = [445]
port7dns = [53]
port8https = [443]
port9http = [80]
port10proxy = [8080]
port11pcsynchttps = [8443]
port19radanhttp  = [8088]
port20dditcp1 = [8888]
port21snmp = [161]
port22ircu = [6669]
port23trojan = [4444]
port12smtp = [25]
port13tftp = [69]
port14aed512 = [149]
port15serialgateway = [1243]
port16seagullais = [1208]
port17iasreg = [2140]
port18nmassesadmin = [3150]
port24sql = [3306]

print("\033[1;37m[#]Scanning 24 ports ...")
system("sleep 1")
print("")

for port in port1ftp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print("\033[1;33mPort | Service | State")
            print("")
            print(f"\033[1;31mPort: \033[1;32m{port} ftp - Open")
        else:
            print("\033[1;33mPort | Service | State")
            print("")
            print(f"\033[1;31mPort: \033[1;32m{port} ftp - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        
for port in port2ssh:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} ssh - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} ssh - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port3telnet:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} telnet - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} telnet - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port4smb:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} smb - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} smb - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port5netbiosns:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} netbios-ns - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} netbios-ns - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port6microsoftds:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} microsoft-ds - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} microsoft-ds - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port7dns:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} dns - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} dns - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port8https:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} https - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} https - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port9http:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} http - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} http - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port10proxy:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} proxy - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} proxy - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port11pcsynchttps:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} pcsync-https - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} pcsync-https - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port19radanhttp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} radan-http - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} radan-http - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port20dditcp1:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} ddi-tcp-1 - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} ddi-tcp-1 - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port21snmp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} snmp - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} snmp - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port22ircu:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} ircu - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} ircu - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port23trojan:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} trojan - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} trojan - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port12smtp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} smtb - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} smtb - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port13tftp:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} tftp - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} tftp - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port14aed512:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} aed-512 - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} aed-512 - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port15serialgateway:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} serialgateway - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} serialgateway - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port16seagullais:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} seagull-ais - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} seagull-ais - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port17iasreg:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} ias-reg - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} ias-reg - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")

for port in port18nmassesadmin:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} nm-asses-admin - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} nm-asses-admin - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        exit()

for port in port24sql:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        status = sock.connect_ex((ip_addr, port))
        if status == 0:
            print(f"\033[1;31mPort: \033[1;32m{port} MySQL - Open")
        else:
            print(f"\033[1;31mPort: \033[1;32m{port} MySQL - Closed")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")
        exit()

print("")
system("bash main.sh")
