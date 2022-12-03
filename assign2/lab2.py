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
        final.append( str(i))
    return final



def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0

    for j in range(len(i)):
      b=((i[j])*(2**i[j]))         
      c=c+b

    l.append(c)
  for x in l:
    m=m+chr(x)
  return m


def BinaryToDecimal(binary):
        
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)   


def toString2(listWithBinaryLists):
    str_data = ""

    for list in listWithBinaryLists:
        decimalData = BinaryToDecimal(int(list))
        str_data = str_data + chr(decimalData)
    return  (str_data)


def Binaryxor(a, b, n):
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


def intToList (data):
    list = []
    for number in data:
        listNumber = []
        while number!=0:
            listNumber.append(number%10);
            number = number//10;
        listNumber.reverse()
        list.append(listNumber)
    return list


def encrypt_basic(method, seed, data, n=''):
    encryptedMessage = "";
    length = len(data)
    if (method == "Solitaire"):
        key = SolitaireKeyGenerator(length,seed);
        bitArrayAfterXor = (xorByteStringWithKey(data, key))
        encryptedMessage = toString2(bitArrayAfterXor)

    if (method == "BlumBlumShub"):
        key = Blum_Blum_Shub_KeyGenerator(length,seed,n);
        bitArrayAfterXor = (xorByteStringWithKey(data, key))
        encryptedMessage = toString2(bitArrayAfterXor)

    return encryptedMessage;



def decrypt_basic(method, seed, data, n=''):
    decryptedMessage = "";
    length = len(data)
    if (method == "Solitaire"):
        key = SolitaireKeyGenerator(length,seed);
        bitArrayAfterXor = (xorByteStringWithKey(data, key))
        decryptedMessage = toString2(bitArrayAfterXor)

    if (method == "BlumBlumShub"):
        key = Blum_Blum_Shub_KeyGenerator(length,seed,n);
        bitArrayAfterXor = (xorByteStringWithKey(data, key))
        decryptedMessage = (toString2(bitArrayAfterXor))

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


def SolitaireKeyGenerator(plaintextLenght, deck):
    
    keyList = [];
    
    key=""

    for _ in range(plaintextLenght):
        

        key = step(deck)
 
        while joker(key):
            key = step(deck)


        keyList.append(numberToBinaryStringForm(key));

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
        numberCurrent = '';
        while (dbBit < 7):
            xCurrent = xList[-1];
            xNext = (xCurrent*xCurrent)%n;
            xList.append(xNext);
            numberCurrent+=str(xNext%2)
            dbBit=dbBit+1;
        keyList.append(numberCurrent);
        db=db+1;
    return keyList;

s,n = generateSandN();

def numberToBinaryStringForm(intNumber):
    numberBinary = "{0:b}".format(int(intNumber))
    while (len(numberBinary)<7):
        numberBinary = '0'+numberBinary

    return str(numberBinary)

