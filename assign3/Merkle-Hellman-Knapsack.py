import random
import utils
import math

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


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.
    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message
    Hint: think about using `zip` at some point
    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints
    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

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
    raise NotImplementedError  # Your implementation here

privKey = (generate_private_key())
publicKey = (create_public_key(privKey));

print (privKey,"\n",publicKey)
