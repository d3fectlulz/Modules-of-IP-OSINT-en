import sys
from random import randint
from os import system
import datetime
import random

system("clear")
system("setterm -foreground red")
print ("")
print ("██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗  ██╗")
print ("██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║  ██║")
print ("███████║███████║██║     █████╔╝ ███████║")
print ("██╔══██║██╔══██║██║     ██╔═██╗ ╚════██|")
print ("██║  ██║██║  ██║╚██████╗██║  ██╗     ██║")
print ("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝")
print ("")

print("\033[1;31m#####################################")
print("\033[1;32m#  Credit card generator            #")
print("\033[1;31m#####################################")
print("\033[1;36m# Edited By : Demo                  #")
print("\033[1;36m# Versión : 1.9                     #")
print("\033[1;36m# Code : PYTHON                     #")
print("\033[1;36m# UKL-TEAM, MRX-TEAM, AND YOU       #")
print("")
bin_format = input("\033[1;32m[~]\033[1;37mEnter the bin: ")
cantidad = input("\033[1;32m[~]\033[1;37mEnter the amount to generate: ")
print("")
print("\033[1;31m#####################################")
print("\033[1;33m#       Generating Targets..        #")
print("\033[1;31m#####################################")
print("")
system("sleep 2")
system("setterm -foreground cyan")

def isValid(card_num):
  sum = 0
  num_digits = len(num_cards)
  pos_even_odd = num_digits

  for i in range(0, num_digits):
    digit = int(card_num[i])
    if not ((i & 1) ^ pos_par_impar):
      digit = digit * 2
    if digit > 9:
      digit = digit - 9
    sum = sum + digit

  return (sum % 10 == 0)

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 16:
    for i in range(15):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCharacter invalid in the format: {}\n".format(bin_format))
        print("The bin format is: xxxxxxxxxxxxxxxx of 16 digits\n")
        sys.exit()

    for i in range(10):
      verifier = cc + str(i)
      if isValid(verifier):
        cc = verifier
        break
      else:
        verifier = cc
  else:
    print("\nERROR: Please insert a valid bin\n")
    print("SOLUTION: The bin format is: xxxxxxxxxxxxxxxx 16 digits\n")
    sys.exit()

  return cc

def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv


def dategen():
    now = datetime.datetime.now()
    date = ""                   
    month = str(randint(1, 9))
    current_year = str(now.year)
    year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
    date = month + "/" + year

    return date

def main():
  for i in range(int(cantidad)):
    cc = generar_cc(bin_format)
    print(f"[Gnd] - {cc} | {dategen()} | {ccv_gen()}")

main()

