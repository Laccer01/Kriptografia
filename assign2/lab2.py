"""
Assignment 2
Group: 524/2
Name: Velican László
Azonosító: vlim2099

"""
import random

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



def Solitaire_encrypt():
    return True;



def Solitaire_decrypt():
    return True;


def Blum_Blum_Shub_encrypt():
    return True;

def Blum_Blum_Shub_decrypt():
    return True;




val=encrypt_basic("mal","123");
decrypt_basic(val,"123");