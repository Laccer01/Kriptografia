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


def encrypt_railfence(plaintext, num_rails):
    rail = [['-1' for i in range(len(plaintext))] for j in range(num_rails)]
     
    dirDownFlag = False
    row = 0
    col = 0
     
    for i in range(len(plaintext)):
        if (row == 0) or (row == num_rails - 1):
            dirDownFlag = not dirDownFlag
         
        rail[row][col] = plaintext[i]
        col += 1
         
        if dirDownFlag:
            row += 1
        else:
            row -= 1

    encrypted_plaintext = ''
    for i in range(num_rails):
        for j in range(len(plaintext)):
            if rail[i][j] != '-1':
                encrypted_plaintext+=rail[i][j]
    return encrypted_plaintext


def decrypt_railfence(ciphertext, num_rails):
    rail = [["-1" for i in range(len(ciphertext))] for j in range(num_rails)]
     
    dirDownFlag = False
    row = 0
    col = 0
     
    for i in range(len(ciphertext)):
        if (row == 0) or (row == num_rails - 1):
            dirDownFlag = not dirDownFlag
         
        rail[row][col] = '*'
        col += 1
         
        if dirDownFlag:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '*') and (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1

    decrypted_plaintext = ''
    row = 0
    col = 0
    for i in range(len(ciphertext)):
         
        if row == 0:
            dirDownFlag = True
        if row == num_rails-1:
            dirDownFlag = False
             
        if (rail[row][col] != '*'):
            decrypted_plaintext += rail[row][col]
            col += 1
             
        if dirDownFlag:
            row += 1
        else:
            row -= 1
    return decrypted_plaintext

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

val1 = encrypt_railfence("WEAREDISCOVEREDFLEEATONCE",3);
val2 = decrypt_railfence(val1,3);
print (val1,val2)

