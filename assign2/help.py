from lab2 import encrypt_basic, decrypt_basic
import sympy
import random


def generateDeck ():
    deck = [];
    for i in range(1,55):
        deck.append(i);
    return deck


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

deck = generateDeck();
x1= (encrypt_basic("Solitaire", deck,"se distinge"))
# print (x1)

# print (decrypt_basic("Solitaire", deck1, x1))

