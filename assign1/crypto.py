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

    encrypted_plaintext = '';
    for i in range(len(plaintext)):
        x =  (chr(ord(plaintext[i])+ord(keywordMultiplied[i])));
        plusszErtek=0;
        if (x>'Z'):
            x = chr(ord(x)-ord('A'))
        if (x>'Z'):
            x = chr(ord(x)-26)
        encrypted_plaintext += x
    return encrypted_plaintext
    decrypted_plaintext
   


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

    decrypted_plaintext = '';
    for i in range(len(ciphertext)):
        x =  ord(ciphertext[i])-ord(keywordMultiplied[i]);
        # print (ord(ciphertext[i])-ord(keywordMultiplied[i]));
        x = chr(x+ord('A'));
        if (x<'A'):
            x = chr(ord(x)+26)
        decrypted_plaintext += x
    return decrypted_plaintext

# Merkle-Hellman Knapsack Cryptosystem

def encrypt_scytale(plaintext, circumference):
    assert len(plaintext) % circumference == 0
    n = len(plaintext)
    columns = n // circumference
    ciphertext = ['-'] * n
    for i in range(n):
        row = i // columns
        col = i % columns
        ciphertext[col * circumference + row] = plaintext[i]
    return "".join(ciphertext)

def decrypt_scytale(ciphertext, circumference):
    
    db=0;
    i=0;
    circumference=circumference-1
    encrypted_plaintext='';
    print (len(ciphertext))
    while (db<len(ciphertext)):
        encrypted_plaintext+=ciphertext[i];
        db=db+1;
        i=i+circumference;
        print (i)
        if (i>=len(ciphertext)):
            i=i-len(ciphertext)+1;
    return encrypted_plaintext


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

# val1 = encrypt_vigenere("APPA", "ONEINPUT")
# print (val1)
# val2=decrypt_vigenere(val1, "ONEINPUT")
# print (val2)

# val1 = encrypt_scytale("IAMHURTVERYBADLYHELP",5)
# # val2 = decrypt_scytale(val1,3)

# print (val1)
# # print (val2)

