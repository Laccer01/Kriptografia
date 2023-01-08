#Név: Velican László
#azonosító: vlim2099
#csoport: 524/2
#Lab4

import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
import sys

megfelel=True

def getMegfelel():
    return megfelel


def uzenetekKuldese():
    global megfelel
    while True:
        message = szerverSocket.recv(1024).decode()
        if ('quitFinal' in message):   
            megfelel = False;     
            break;
        
        print(message)


init()                                                                  # színek inicializálása

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,   # elérhető színek
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

kliensSzine = random.choice(colors)    # véletlenszerű szín a kliensnek

if (len(sys.argv)!=3):                                                  #ha helyesen van megadva a port és host
    print ("Hasznalat: python Kliens.py <host> <port>")
    exit (1)


szerverHost = str(sys.argv[1])                                          #megadott host név
szerverPort = int(sys.argv[2])                                          #megadott port
elvalasztoElem = "<SEP>"                                                # elválasztó

szerverSocket = socket.socket()                                         #létrehozzuk a socketet
print(f"[?] Csatakozás: {szerverHost}:{szerverPort}...")
szerverSocket.connect((szerverHost, szerverPort))                       # csatlakozunk a szerverre

print("[+] Sikerült csatlakozni a szerverhez.")
name = input("Felhasználónév: ")                                        # felhasználónév bekérése
szerverSocket.send(name.encode())   
message = szerverSocket.recv(1024).decode()      
while ('repeat' in message):   
            name = input("A felhasználónév foglalt, válassz egy másik nevet: ")
            szerverSocket.send(name.encode())   
            message = szerverSocket.recv(1024).decode()     

else:                                        # felhasználónév bekérése
    print ('Üdv \n1. Nyílvános kulcs lekérése (lekerdez client-id)\n2. Regisztrálj a szervernél(regisztral client_id nyílvános_kulcs)\n')

    kliensSzal = Thread(target=uzenetekKuldese)                             # szál létrehozása
    kliensSzal.daemon = True                                                # legyen a szál daemon azért hogy ha véget ér a főszáll akkor érjen végett az adott szál is
    kliensSzal.start()                                                      # szál indítása

    while (True & getMegfelel()==True):
        kuldendoUzenet =  input()                                                  #szervernek küldhetünk üzenetet

        jelenlegiDatum = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

        kuldendoUzenet = f"{kliensSzine}[{jelenlegiDatum}] {name}{elvalasztoElem}{kuldendoUzenet}{Fore.RESET}"    #hozzáadjuk a színt, küldő nevét és a dátumot is a küldendő üzenethez

        szerverSocket.send(kuldendoUzenet.encode())                                #elküldjük az üzenetet

szerverSocket.close()