#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Velican László
SUNet: vlim2099

Replace this with a description of the program.
"""
import utils

# Caesar Cipher

def encrypt_caesar(plaintext):
    encrypted_plaintext ='';
    for i in range(0,len(plaintext)):
        encrypted_plaintext += chr(ord(plaintext[i]) + 3)

        if (encrypted_plaintext[i] > 'Z'):
            my_list = list(encrypted_plaintext)
            my_list[i] = chr(ord(encrypted_plaintext[i]) - 26)
            encrypted_plaintext = ''.join(my_list)
    
    return encrypted_plaintext  # Your implementation here


def decrypt_caesar(ciphertext):
    decrypted_plaintext ='';
    for i in range(0,len(ciphertext)):
        decrypted_plaintext += chr(ord(ciphertext[i]) - 3)
    
        if (decrypted_plaintext[i] < 'A' and decrypted_plaintext[i] < 'Z'):
            my_list = list(decrypted_plaintext)
            my_list[i] = chr(ord(decrypted_plaintext[i]) + 26)
            decrypted_plaintext = ''.join(my_list)

    return decrypted_plaintext  # Your implementation here


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):

    n=1;
    m=0;
    keywordMultiplied='';
    if (len(keyword)<len(plaintext)):
        n=len(plaintext)//len(keyword)
        m=len(plaintext)%len(keyword)

    for i in range(0,n):
        keywordMultiplied=keywordMultiplied+keyword;
    for i in range(0,m):
        keywordMultiplied=keywordMultiplied+keyword[i];

    encryptedText = '';
    for i in range(len(plaintext)):
        x =  (chr(ord(plaintext[i])+ord(keywordMultiplied[i])));
        plusszErtek=0;
        if (x>'Z'):
            x = chr(ord(x)-ord('A'))
        if (x>'Z'):
            x = chr(ord(x)-26)
        encryptedText += x
    return encryptedText
   


def decrypt_vigenere(ciphertext, keyword):
    n=1;
    m=0;
    keywordMultiplied='';
    if (len(keyword)<len(ciphertext)):
        n=len(ciphertext)//len(keyword)
        m=len(ciphertext)%len(keyword)

    for i in range(0,n):
        keywordMultiplied=keywordMultiplied+keyword;
    for i in range(0,m):
        keywordMultiplied=keywordMultiplied+keyword[i];

    encryptedText = '';
    for i in range(len(ciphertext)):
        x =  ord(ciphertext[i])-ord(keywordMultiplied[i]);
        # print (ord(ciphertext[i])-ord(keywordMultiplied[i]));
        x = chr(x+ord('A'));
        if (x<'A'):
            x = chr(ord(x)+26)
        encryptedText += x
    return encryptedText

# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


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

# encr_caesar = encrypt_caesar("PYTHON")
# decr_caesar = decrypt_caesar(encr_caesar)
# print (encr_caesar+"\n"+decr_caesar)

val1 = encrypt_vigenere("APPA", "ONEINPUT")
print (val1)
val2=decrypt_vigenere(val1, "ONEINPUT")
print (val2)
