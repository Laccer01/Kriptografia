import random
import math
import utils

def findCoprimePair(N):

    for x in range(2, int(math.sqrt(N)) + 1):
        if (N % x == 0):
            while (N % x == 0):
                N //= x
 
            if (N > 1):
 
                return x

def generate_private_key(n=8):
    global w, q, r

    w = [1]
    z = 1
    for i in range(n):
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

    for i in range (n):
        beta.append((r * w[i])%q)
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

    for chunk in chunks:
        betuChunk=''
        for betu in chunk:
            array = toBinary(betu)
            c=0;
            for i in range (0,8):
                c=c+int(array[i])*int(public_key[i]);
            betuChunk+=toString2(str(c))
        print (betuChunk)


    #raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key
    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back
    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r
    @return bytearray or str of decrypted characters
    """

    w=private_key[0];
    q=private_key[1];
    r=private_key[2];
    s = utils.modinv(r,q)
    raise NotImplementedError  # Your implementation here

privKey = (generate_private_key())
publicKey = (create_public_key(privKey));

#print (privKey,"\n",publicKey)

encrypt_mh("abracadabraaaaaas",publicKey)

#xorByteStringWithKey("aha",2);
#print (toString2('01100001'))
