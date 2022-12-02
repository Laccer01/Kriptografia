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
from lab2 import encrypt_basic, decrypt_basic


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
        # decodedMessage = decrypt_basic(encrypName,s,kuldendoUzenet,n)
        print("Az uzenet kodolva: " + message)
        # print("Az uzenet vissza kodolva: " + decodedMessage)

def beolvasEncryptalas():
    configFile = open("config", "r")
    encrypName = configFile.readline()
    print (encrypName)
    n = configFile.read();
    s = configFile.read();
    return encrypName, n, s;

encrypName, n, s = beolvasEncryptalas();

init()                                                                  # színek inicializálása

colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,   # elérhető színek
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

kliensSzine = random.choice(colors)    # véletlenszerű szín a kliensnek

if (len(sys.argv)!=3):                                                  #ha helyesen van megadva a port és host
    print ("Hasznalat: python vlim2099_szerver.py <host> <port>")
    exit (1)


encrypName, n, s = beolvasEncryptalas();

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
    print ('Üdv a chat szerveren, néhány tudnivaló:\n1. Ha nyilvános üzenetet szeretnél küldeni, amit mindenki fog látni a részvevők közül akkor csak írj egy üzenetet és enter segítségével elküldheted\n' +
        '2. Ha privát üzenetet szeretnél küldeni -> (p) (felhasznalo neve) üzenet formájában teheted meg\n3. Ha meg szeretnél nézni a szerveren levő emberek listáját -> online-list\n4. Ha ki akarsz lépni a szerverről -> quit\n\n')

    kliensSzal = Thread(target=uzenetekKuldese)                             # szál létrehozása
    kliensSzal.daemon = True                                                # legyen a szál daemon azért hogy ha véget ér a főszáll akkor érjen végett az adott szál is
    kliensSzal.start()                                                      # szál indítása

    while (True & getMegfelel()==True):
        kuldendoUzenet =  input()                                                  #szervernek küldhetünk üzenetet
        encryptaltKuldendoUzenet = encrypt_basic(encrypName,s,kuldendoUzenet,n)
        print (encryptaltKuldendoUzenet)
        print (encrypName,n,s)
        jelenlegiDatum = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

        encryptaltKuldendoUzenet = f"{kliensSzine}[{jelenlegiDatum}] {name}{elvalasztoElem}{kuldendoUzenet}{Fore.RESET}"    #hozzáadjuk a színt, küldő nevét és a dátumot is a küldendő üzenethez

        szerverSocket.send(encryptaltKuldendoUzenet.encode())                                #elküldjük az üzenetet

szerverSocket.close()