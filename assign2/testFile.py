"""
Assignment 2
Csoport: 524/2
Név: Velican László
Azonosító: vlim2099

Függvények kipróbálása

"""


from lab2 import encrypt_basic, decrypt_basic, Blum_Blum_Shub_KeyGenerator, SolitaireKeyGenerator
from auxiliaryFunctions import *

dataFromFile = beolvasEncryptalas();
encryptedText = encrypt_basic(dataFromFile[0], dataFromFile[1], "utolso teszt 123")
dataFromFile = beolvasEncryptalas();                                                    #mivel a deck elromlik ezert olvassuk ki az eredetit a config fileból
decryptedText = decrypt_basic(dataFromFile[0], dataFromFile[1], encryptedText)

print (encryptedText + "\n" + decryptedText)


generatedDeck = generateDeck()
generatedDeckCopy = generateDeck()
print ("\nA generalt pakli", generatedDeck)

generatedSeed = generateSeed()
print ("\nA generalt seed", generatedSeed)

keyBlumBlumShub = Blum_Blum_Shub_KeyGenerator(5, generatedSeed)
print ("\nA generalt kulcs Blum-Blum-Shub-al", keyBlumBlumShub)

keySolitaire = SolitaireKeyGenerator(5, generatedDeck)
print ("\nA generalt kulcs Solitaire-al", keySolitaire)

plainText = "utolso teszt"
BlumBlumShubEncryptedText = encrypt_basic("BlumBlumShub", generatedSeed, plainText)
BlumBlumShubDecryptedText = decrypt_basic("BlumBlumShub", generatedSeed, BlumBlumShubEncryptedText)
print ("Encryptalt Blum-Blum-Shub kulccsal: ", BlumBlumShubEncryptedText)
print ("Decryptalt Blum-Blum-Shub kulccsal: ", BlumBlumShubDecryptedText)


generatedDeck = generateDeck()
generatedDeckCopy = generateDeck()

SolitaireEncryptedText = encrypt_basic("Solitaire", generatedDeck, plainText)
SolitaireDecryptedText = decrypt_basic("Solitaire", generatedDeckCopy, SolitaireEncryptedText)
print ("\nEncryptalt Solitaire kulccsal: ", SolitaireEncryptedText)
print ("Decryptalt Solitaire kulccsal: ", SolitaireDecryptedText)
