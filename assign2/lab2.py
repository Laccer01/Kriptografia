"""
Assignment 2
Group: 524/2
Name: Velican László
Azonosító: vlim2099

"""
import random
import sympy

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
 




def Blum_Blum_Shub_KeyGenerator(plaintextLenght):
    keyList = [];
    xList = [];
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
    x0 = (s*s)%n
    xList.append(x0);

    db = 0;
    while (db<plaintextLenght):
        dbBit = 0;
        numberCurrent = [];
        while (dbBit < 7):
            xCurrent = xList[-1];
            xNext = (xCurrent*xCurrent)%n;
            xList.append(xNext);
            numberCurrent.append(xNext%2);
            dbBit=dbBit+1;
        keyList.append(numberCurrent);
        db=db+1;
    return keyList;


def toBinary(a):
  l,m,final=[],[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))

    for i in m:
        final.append(list(map(int, str(i))))
  return final


def binAdd(s1, s2):
    if not s1 or not s2:
        return ''

    result  = ''
    carry   = 0

    i = 7 - 1
    while(i >= 0):
        s = s1[i] + s2[i]
        if s == 2: #1+1
            if carry == 0:
                carry = 1
                result = "%s%s" % (result, '0')
            else:
                result = "%s%s" % (result, '1')
        elif s == 1: # 1+0
            if carry == 1:
                result = "%s%s" % (result, '0')
            else:
                result = "%s%s" % (result, '1')
        else: # 0+0
            if carry == 1:
                result = "%s%s" % (result, '1')
                carry = 0   
            else:
                result = "%s%s" % (result, '0') 

        i = i - 1;

    if carry>0:
        result = "%s%s" % (result, '1')
    return result[::-1]     


x3=(toBinary("Hello"))

# print (SolitaireKeyGenerator(11,99))
x1=(Blum_Blum_Shub_KeyGenerator(2))
x2=(Blum_Blum_Shub_KeyGenerator(2))
print (x3)


# val=encrypt_basic("mal","123");
# decrypt_basic(val,"123");