"""
Assignment 2
Csoport: 524/2
Név: Velican László
Azonosító: vlim2099

Solitaire

"""
from auxiliaryFunctions import *
#átalakít egy stringet 7 hosszúságu bit streingekké
def toBinary(a):
    
    l,m,final=[],[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))

    for i in m:
        final.append( str(i))
    return final

#átalakít egy bináris számot decimális számmá
def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)   

#átalakí egy listát amiben 7 karakter hosszúságu bit stringek vannak, amelyből karakterek lesznek
def toString2(listWithBinaryLists):
    str_data = ""

    for list in listWithBinaryLists:
        decimalData = BinaryToDecimal(int(list))
        str_data = str_data + chr(decimalData)
    return  (str_data)

#XOR művelet két bit string között (melyek 7 karakter hosszúak, ha nincs megadva a 3.paraméter)
def Binaryxor(a, b, n = 7):
    ans = ""
    while (len(a)!=n):
        a='0'+a;

    while (len(b)!=n):
        b='0'+b
    for i in range(n):
         
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans

#XOR művelet egy kulcs és egy string között
def xorByteStringWithKey (string, key):                      
    encryptedBitArray = []

    n = len(string)
    db = 0;
    while (db<n):
        currentLetter = string[db];
        currentLetterBitArray = toBinary(currentLetter)[0];

        currrentIndexAddedinList =  (Binaryxor(currentLetterBitArray, str(key[db]),7))
        encryptedBitArray.append((currrentIndexAddedinList))
        db=db+1;

    return encryptedBitArray

#átlakít egy számot egy bit számmá string formátumban
def numberToBinaryStringForm(intNumber):
    numberBinary = "{0:b}".format(int(intNumber))
    while (len(numberBinary)<7):
        numberBinary = '0'+numberBinary

    return str(numberBinary)

#általános, bájtsorozatot kódoló/dekódoló folyamtitkosítót
def encrypt_solitaire(seed, data):
    encryptedMessage = "";
    length = len(data)
    
    key = SolitaireKeyGenerator(length,seed);

    bitArrayAfterXor = (xorByteStringWithKey(data, key))
    encryptedMessage = toString2(bitArrayAfterXor)

    return encryptedMessage;


def decrypt_solitaire(seed, data):
    decryptedMessage = "";
    length = len(data)
   
    key = SolitaireKeyGenerator(length,seed);

    bitArrayAfterXor = (xorByteStringWithKey(data, key))
    decryptedMessage = (toString2(bitArrayAfterXor))

    return decryptedMessage;


# Solitaire 
def movedown(deck,entry,move):          #lejebb mozgat egy kártyát a pakliban

    newindex = deck.index(entry) + move
    if newindex >= len(deck):
        newindex -= len(deck) - 1
    deck.remove(entry)
    deck.insert(newindex,entry)
 
def countcut(deck,count):               #az alsó kártya száma alapján, a felső számlálókártyákat az alsó fölé helyezzük
  
    deck[-1:1] = deck[:count]
    del(deck[:count])
 
def joker(card):                    #vizsgálom ha a kartya joker kártya e
    return card in (53, 54)
 
def step(deck):                     #végrehajt egy lépést a paklin és visszatéríti a kulcsot
 
    movedown(deck,53,1)             #mozgatja a két jokert lejebb a pakliban, ha kell a pakli aljára
    movedown(deck,54,2)

    indexa = deck.index(53)         #triple vágás: felcseréli az összes kártyát a felső joker fölött az összes kártyával az alsó joker alatt
    indexb = deck.index(54)         #-> így a két joker és a köztük levő távolság nem fog változni 
 
    if indexb > indexa:
        topindex, botindex = indexa, indexb
    else:
        topindex, botindex = indexb, indexa
 
    deck.extend(deck[topindex:botindex + 1])
    deck.extend(deck[:topindex])
    del(deck[:botindex + 1])
 
    count = deck[-1]                #egy számolt vágás, az alsó lap száma alapján
                                    #kártyák 1-től 52-ig vannak számozva híd sorrendben
                                    #bármelyik joker 53-nak számít
     
    if joker(count):
        count = 53
    countcut(deck,count)

    count = deck[0]                 #a legfelső kártya alapján vissza kell számolni lapokat és az aktuális kártya lesz a kulcskártya.     
    if joker(count):
        count = 53
     
    return deck[count]
 

#kulcs generálás Solitaire segítségével
def SolitaireKeyGenerator(plaintextLenght, deck):
    
    keyList = [];
    key=""
    for _ in range(plaintextLenght):
        key = step(deck)
        while joker(key):
            key = step(deck)

        keyList.append(numberToBinaryStringForm(key));

    return keyList;
 



generatedDeck = generateDeck()
generatedDeckCopy = generateDeck()
print ("\nA generalt pakli", generatedDeck)


keySolitaire = SolitaireKeyGenerator(5, generatedDeck)
print ("\nA generalt kulcs Solitaire-al", keySolitaire)

plainText = "utolso teszt"
generatedDeck = generateDeck()
generatedDeckCopy = generateDeck()

SolitaireEncryptedText = encrypt_solitaire(generatedDeck, plainText)
SolitaireDecryptedText = decrypt_solitaire(generatedDeckCopy, SolitaireEncryptedText)
print ("\nEncryptalt Solitaire kulccsal: ", SolitaireEncryptedText)
print ("Decryptalt Solitaire kulccsal: ", SolitaireDecryptedText)
