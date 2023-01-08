import socket
from threading import Thread
import sys
from pathlib import Path
import os


if (len(sys.argv)!=3):                                                  #ha helyesen van megadva a port és host
    print ("Hasznalat: python KeyServer.py <host> <port>")
    exit (1)


szerverHost = str(sys.argv[1])                                          #megadott host név
szerverPort = int(sys.argv[2])    
elvalaszto = "<SEP>"                                                # elválasztó


kliensSocketek = set()                                                  # csatlakozott socketek
kliensnevNyilvanoskulcs = {}
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
                
                if ('lista' in msg):
                    lista = ""
                    for nev in hasznaltFelhasznalonevek:
                        lista += nev + ", "
                    cs.send(lista.encode())    
                else:
                    if ('lekerdez' in msg):
                        szavak = msg.split(' ')
                        privatSzemely = szavak[4][:-5]
                        if (privatSzemely in kliensnevNyilvanoskulcs):
                            cs.send(kliensnevNyilvanoskulcs[privatSzemely].encode())   
                        else:
                            cs.send("Ez a személy nincs regisztrálva".encode())   
                        
                       
                    else:
                        if ('regisztral' in msg):
                            szavak = msg.split(' ')
                            szemely = szavak[4]
                            publikusKulcs = szavak[5]                   
                            if (szemely in kliensnevNyilvanoskulcs): 
                                kliensnevNyilvanoskulcs[szemely]=publikusKulcs;       
                                cs.send("A felhasználó publikus kulcsa frissült".encode())
                            else:
                                kliensnevNyilvanoskulcs[szemely]=publikusKulcs;       
                                cs.send("Sikeres regisztracio".encode())

                        else:
                            cs.send("Hibas keres".encode())
                                
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

