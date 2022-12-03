import socket
from threading import Thread
import sys
from pathlib import Path
import os

from lab2 import encrypt_basic, decrypt_basic
from generateFunctions import beolvasEncryptalas

if (len(sys.argv)!=3):                                                  #ha helyesen van megadva a port és host
    print ("Hasznalat: python vlim2099_szerver.py <host> <port>")
    exit (1)


szerverHost = str(sys.argv[1])                                          #megadott host név
szerverPort = int(sys.argv[2])    
elvalaszto = "<SEP>"                                                # elválasztó


kliensSocketek = set()                                                  # csatlakozott socketek
socketFelhasznalonev = {}
hasznaltFelhasznalonevek = []


szerverSocket = socket.socket()                                         # szerver socket
szerverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
szerverSocket.bind((szerverHost, szerverPort))                          #bind a megfelelő host-port - ra

szerverSocket.listen(25)                                                # 25 klienset tud kiszolgálni, várja ezeket
print(f"[*] A szerver elindult: {szerverHost}:{szerverPort}")

def kliensUzenete(cs, client_address):
  
    msg = cs.recv(1024).decode()
    while (msg in hasznaltFelhasznalonevek):
        cs.send("repeat".encode())
        msg = cs.recv(1024).decode()

    else:
        cs.send("okes".encode())
        hasznaltFelhasznalonevek.append(msg)

        while True:
            try:
                msg = cs.recv(1024).decode()
                szavak = msg.split()
                szavak1 = szavak[2].split('<')
                
                socketFelhasznalonev[szavak1[0]] = cs;
            
                msg = msg.replace(elvalaszto, ": ")
                messageSpliitedList = msg.split(' ');
                messageSpliited = messageSpliitedList[len(messageSpliitedList)-2]
                print (messageSpliited)

                dataFromFile = beolvasEncryptalas();
                messageSpliitedEncrypted = encrypt_basic(dataFromFile[0], dataFromFile[1], messageSpliited)
                
                
                if ('quit' in messageSpliitedEncrypted):
                    socketFelhasznalonev.pop(szavak1[0])    
                    print ('Kilepett a felhasznalo: ' + str(szavak1[0]))
                    
                    hasznaltFelhasznalonevek.remove(szavak1[0])
                    
                    cs.send("quitFinal".encode())

                    break;
                else:
    
                    for client_socket in kliensSocketek:
                        client_socket.send(msg.encode())
                                
            except Exception as e:

                
                if (not (cs in kliensSocketek)):
                    kliensSocketek.remove(cs)
                    break;

            


try:
    while True:
        client_socket, client_address = szerverSocket.accept()                        #várjuk a kliensek kéréseit
        print(f"[+] {client_address} sikeresen kapcsolódott.")

        kliensSocketek.add(client_socket)                                             #hozzáadjuk a kliens socketet a listához       
        kliensSzal = Thread(target=kliensUzenete, args=(client_socket,client_address,))                   #indítunk minden kliensnek egy új szálat
        kliensSzal.daemon = True                                                               # legyen a szál daemon azért hogy ha véget ér a főszáll akkor érjen végett az adott szál is       
        kliensSzal.start()   
                                                           # szál indítása
except Exception as e:
    print (e)

for cs in kliensSocketek:
    cs.close()

szerverSocket.close()

