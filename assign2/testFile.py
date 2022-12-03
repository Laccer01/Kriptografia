from lab2 import encrypt_basic, decrypt_basic
from generateFunctions import generateDeck

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

dataFromFile = beolvasEncryptalas();
encryptedText = encrypt_basic(dataFromFile[0], dataFromFile[1], "valami tortenik")
dataFromFile = beolvasEncryptalas();                                                    #mivel a deck elromlik ezert olvassuk ki az eredetit a config fileból
decryptedText = decrypt_basic(dataFromFile[0], dataFromFile[1], encryptedText)

print (encryptedText + "\n" + decryptedText)
