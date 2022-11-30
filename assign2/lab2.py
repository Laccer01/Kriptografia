"""
Assignment 2
Group: 524/2
Name: Velican László
Azonosító: vlim2099

"""
import random
import sympy

def toBinary(a):
    l,m,final=[],[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))

    for i in m:
        final.append(list(map(int, str(i))))
    return final


import math

def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m




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


def binarySubstration(str1,str2):


    startIdx = 0
    endIdx = len(str1)-1
    carry = [0] * len(str1)
    result = ''

    while endIdx >= startIdx:
        x = int(str1[endIdx])
        y = int(str2[endIdx])
        sub = (carry[endIdx] + x) - y
        
        if sub == -1:
            result += '1'
            carry[endIdx-1] = -1

        elif sub == 1:
            result += '1'
        elif sub == 0:
            result += '0'
       
        endIdx -= 1
    
    return result[::-1]

# def convert(list):
     
#     s = [str(i) for i in list]
#     res = int("".join(s)) 
#     return(res)

def xorByteStringWithKey (string, key):
    encryptedBitArray = []

    n = len(string)
    db = 0;
    while (db<n):
        currentLetter = string[db];
        currentLetterBitArray = toBinary(currentLetter);
        currentIndexAdded = binAdd(currentLetterBitArray[0], key[db]);
        if (len(currentIndexAdded)>7):
            currentIndexAdded = currentIndexAdded[1:]
        encryptedBitArray.append(int(currentIndexAdded))
        db=db+1;

    return encryptedBitArray


def xorByteStringWithKeyMinus (string, key):
    decryptedBitArray = []

    n = len(string)
    db = 0;
    while (db<n):
        currentLetter = string[db];
        currentLetterBitArray = toBinary(currentLetter);
        currentIndexAdded = binarySubstration(currentLetterBitArray[0], key[db]);
        decryptedBitArray.append(int(currentIndexAdded))
        db=db+1;

    return decryptedBitArray
# def byte_xor(ba1, ba2):
#     return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


# def PRNG(seed):
#     random.seed(seed)
#     return random.randint(0, 1000);


def generateSandN ():
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

    return s,n;


def encrypt_basic(method, seed, data, n=''):
    encryptedMessage = "";
    length = len(data)
    if (method == "Solitaire"):
        return True;

    if (method == "Blum_Blum_Shub"):
        key = Blum_Blum_Shub_KeyGenerator(length,seed,n);
        bitArrayAfterXor = (xorByteStringWithKey(data, key))
        encryptedMessage = (toString(bitArrayAfterXor))
        print (key)

    return encryptedMessage;


def decrypt_basic(method, seed, data, n=''):
    decryptedMessage = "";
    length = len(data)
    if (method == "Solitaire"):
        return True;

    if (method == "Blum_Blum_Shub"):
        key = Blum_Blum_Shub_KeyGenerator(length,seed,n);
        bitArrayAfterXor = (xorByteStringWithKeyMinus(data, key))
        decryptedMessage = (toString(bitArrayAfterXor))

        print (key)

    return decryptedMessage;



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
 

# Blum Blum Shub ----------------------------------------------------------------------------------------------------------------


def Blum_Blum_Shub_KeyGenerator(plaintextLenght, s, n):
    keyList = [];
    xList = [];
    
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



# x3=(toBinary("Hello"))

# # print (SolitaireKeyGenerator(11,99))
# x1=(Blum_Blum_Shub_KeyGenerator(2))
# x2=(Blum_Blum_Shub_KeyGenerator(2))
# print (x3)










s,n = generateSandN();

# print (Blum_Blum_Shub_KeyGenerator(8, s, n))
# print (Blum_Blum_Shub_KeyGenerator(8, s, n))

x1 = (encrypt_basic("Blum_Blum_Shub", s, "aa", n))
print (toBinary("a"))
print (toBinary(x1))
print (x1)
print (decrypt_basic("Blum_Blum_Shub", s, x1, n))

# 

# print(binarySubstration([1,0,0,0],[0,0,0,1]))
# val=encrypt_basic("mal","123");
# decrypt_basic(val,"123");