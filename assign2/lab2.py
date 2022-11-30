"""
Assignment 2
Group: 524/2
Name: Velican László
Azonosító: vlim2099

"""
import random

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def PRNG(seed):
    random.seed(seed)
    return random.randint(0, 1000);


def encrypt_basic(message):
    messageBytes = bytes(message, 'utf-8')
    keyBytes = bytes(key, 'utf-8')
    encryptedMessage = byte_xor(messageBytes,keyBytes)
    
    print("original string: ", message)
    print("encrypted string: ", encryptedMessage)
    

    return encryptedMessage;


def decrypt_basic(messageBytes, key):
    
    keyBytes = bytes(key, 'utf-8')
    decryptedMessage = (byte_xor(messageBytes,keyBytes)).decode("utf-8");
    
    print("original string: ", messageBytes)
    print("decrypted: ", decryptedMessage)
    

    return decryptedMessage


# Solitaire ---------------------------------------------------------------------------------------------------------------------------

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
 

    #mozgatja a két jokert
    movedown(deck,53,1)
     
    movedown(deck,54,2)


    # triple-cut
    indexa = deck.index(53)
    indexb = deck.index(54)
 
    if indexb > indexa:
        topindex, botindex = indexa, indexb
    else:
        topindex, botindex = indexb, indexa
 
    deck.extend(deck[topindex:botindex + 1])
    deck.extend(deck[:topindex])
    del(deck[:botindex + 1])
 

    #count cut
    count = deck[-1]
     
    if joker(count):
        count = 53
     
    countcut(deck,count)

    count = deck[0]
     
    if joker(count):
        count = 53
     
    return deck[count]
 
 

def randomizeDeck (deck, seed):

    return random.Random(seed).shuffle(deck)


def SolitaireKeyGenerator(plaintextLenght, seed):

     
    deck = [];
    keyList = [];
    for i in range(1,55):
        deck.append(i);

    key=""
  
    for _ in range(plaintextLenght):
        
        seed = random.randrange(seed*seed)	

        randomizeDeck(deck, seed);
        key = step(deck)
 
        while joker(key):
            key = step(deck)

        keyList.append(key);


    return keyList;
 




def Blum_Blum_Shub_KeyGenerator():
    return True;




print (solitare(11,99))
# val=encrypt_basic("mal","123");
# decrypt_basic(val,"123");