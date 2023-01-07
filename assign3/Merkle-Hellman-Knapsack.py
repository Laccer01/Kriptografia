import random
import math
import utils
import itertools

def getAllCombinations(lista):
    combinations = []
    for r in range(len(lista)+1):
        for combination in itertools.combinations(set(lista), r):
            combinations.append(combination)
    return combinations

def are_coprime(a,b):
    
    hcf = 1

    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf = i

    return hcf == 1

def prime (x):
    if(x > 1): 
        for k in range(2, int(math.sqrt(x)) + 1): 
            if (x % k == 0): 
                return False;
                
    return True;


def findCoprimePair(N):

    for x in range(int(math.sqrt(N)) + 1,2,-1):
        if (are_coprime(N,x) and prime(x)):
            return x;

def generate_private_key(n=8):
    global w, q, r

    w = [1]
    z = 1
    for i in range(0,n-1):
        total = sum(w[:])
        z = random.randint(total + 1, 2 * total)
        w.append(z)
    
    w = tuple(w)

    total = sum(w[:])
    q = random.randint(total + 1, 2 * total)

    r=findCoprimePair(q)

    return (w, q, r)

def create_public_key(private_key):
    beta = []
    w=private_key[0];
    q=private_key[1];
    r=private_key[2];
    n=8;
    # print (private_key)
    # print ()
    for i in range (n):
        beta.append((r * w[i])%q)
    # print (beta)
    return tuple(beta)

def toBinary(a):
    
    res = ''.join(format(ord(i), '08b') for i in a)
    return res;

def BinaryToDecimal(binary):
        
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)  

def toString2(bin_data):
    str_data=''
    for i in range (0, len(bin_data), 8):
        temp_data = int(bin_data[i:i + 8])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
        return str_data;


def encrypt_mh(message, public_key):
  
    chunks = [message[i:i+8] for i in range(0, len(message), 8)]
    #print (chunks)
    chunksFull = []
    for chunk in chunks:
        betuChunk=[]
        for betu in chunk:
            array = toBinary(betu)
            c=0;
            for i in range (0,8):
                c=c+int(array[i])*int(public_key[i]);
            # print (c)
            betuChunk.append(c)
            # print (betuChunk)
            # print (ord(betuChunk))
            # print (toBinary((betuChunk)))
        
        return (betuChunk)

def modInverse(A, M):
     
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def visszaSzamol (kombinaciok, szam):
    megfelel = False;
    # szamMasolat=szam;
    for lista in kombinaciok:
        szamMasolat=szam;
        for j in lista:
            szamMasolat=szamMasolat-j;
        if (szamMasolat==0):
            return lista
            break;
        
        
def kialakitEredmeny (listaPrivateKey, megfeleloLista):
    megoldas=''
    for szam in listaPrivateKey:
        if (szam in megfeleloLista):
            megoldas+='1';
        else:
            megoldas+='0'
    return megoldas;


def decrypt_mh(message, private_key):
    
    w=private_key[0];
    q=private_key[1];
    r=private_key[2];
    #print (r,q)
    s = modInverse(r,q)
    #print (s)
    # print (list(w))
    chunks = [message[i:i+8] for i in range(0, len(message), 8)]
    for chunk in chunks:
        betuChunk=''
        for betuErtek in chunk:
            szam=(betuErtek*s)%q;
            # print (szam)
            #itt kene visszalakitani a privat kulccsal a binaris kodot
            komb = (getAllCombinations(list(w)))
            megfeleloTomb = (visszaSzamol(komb,szam));
            eredmeny = ((kialakitEredmeny(list(w), megfeleloTomb)));
            betuChunk+= (toString2(str(eredmeny)))

    return betuChunk

privKey = (generate_private_key())
publicKey = (create_public_key(privKey));

# print (privKey,"\n",publicKey)
#print (modInverse(50 ,2443))

#print (toString2('01100001'))

# print("\n\n")
kar=encrypt_mh("abcdefgh",publicKey)
# print ('a', ord('a'))
print (kar)
kar2 = decrypt_mh(kar,privKey)
print (kar2)

#print (kar)
#xorByteStringWithKey("aha",2);

# komb = (getAllCombinations([1,2,3]))
# print (visszaSzamol(komb,3));