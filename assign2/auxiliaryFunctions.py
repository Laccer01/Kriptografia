from lab2 import encrypt_basic, decrypt_basic
import sympy
import random

def generateDeck ():
    deck = [];
    for i in range(1,55):
        deck.append(i);
    return deck

def shuffleDeck (deck):
    n = len(deck)
    for i in range(n-1,0,-1):
        j = random.randint(0,i+1)
        deck[i],deck[j] = deck[j],deck[i]
    return deck

def copyByValue (variable):
    return variable
    
def generateSeed ():
    p=-1;
    q=-1;
    start = 999999999;
    while (p==-1):
        x = sympy.nextprime(start);
        if(x % 4 == 3):
            p=x;
        start = x+1

    while (q==-1):
        x = sympy.nextprime(start);
        if(x % 4 == 3):
            q=x;
        start = x+1
        
    n=p*q
    s = random.randint(1, n-1)
    return s;

def beolvasEncryptalas():
    configFile = open("config", "r")
    dataFromFile = configFile.read().splitlines()
    if (dataFromFile[0]=="BlumBlumShub"):
        dataFromFile[1] = int(dataFromFile[1])
    else:
        listaString =  dataFromFile[1]
        if (listaString[0]=='[' and listaString[len(listaString)-1]==']'):
            listaString = listaString[1:-1]
        deckLista = listaString.split(", ");
        deckLista = [int(i) for i in deckLista]
        dataFromFile[1] = deckLista;
    return dataFromFile; 

