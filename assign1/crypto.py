#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Velican László
SUNet: vlim2099

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
    
    return encrypted_plaintext  


def decrypt_caesar(ciphertext):
    decrypted_plaintext ='';
    for i in range(0,len(ciphertext)):
        decrypted_plaintext += chr(ord(ciphertext[i]) - 3)
    
        if (decrypted_plaintext[i] < 'A' and decrypted_plaintext[i] < 'Z'):
            my_list = list(decrypted_plaintext)
            my_list[i] = chr(ord(decrypted_plaintext[i]) + 26)
            decrypted_plaintext = ''.join(my_list)

    return decrypted_plaintext  


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

        x = chr(x+ord('A'));
        if (x<'A'):
            x = chr(ord(x)+26)
        decrypted_plaintext += x
    return decrypted_plaintext


def encrypt_scytale(plaintext, circumference):
    encrypted_plaintext = '';
    n = len(plaintext)
    for i in range(circumference):
        j=0;
        while (i+j*circumference < n):
            encrypted_plaintext += plaintext[i+j*circumference];
            j+=1;

    return encrypted_plaintext

def decrypt_scytale(ciphertext, circumference):
    decrypted_plaintext = '';
    n = len(ciphertext)
    iteration = n//circumference;
  
    for i in range(iteration):
        j=0;
        while (i+j*iteration < n):
            decrypted_plaintext += ciphertext[i+j*iteration];
            j+=1;

    return decrypted_plaintext    


def encrypt_railfence(plaintext, num_rails):
    encrypted_plaintext = '';
    n = len(plaintext)
    num_rails_dinamic = num_rails;
 
    i=0;
    while (num_rails_dinamic>=0):
        currentPosition=i;
        while (currentPosition < n):
    
            encrypted_plaintext += plaintext[currentPosition];
            currentPosition += num_rails_dinamic+1
            
        num_rails_dinamic = num_rails_dinamic-2
        i+=1;
     

    currentPosition=i;
    while (currentPosition < n):
        encrypted_plaintext += plaintext[currentPosition];
        currentPosition += num_rails+1
                
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



