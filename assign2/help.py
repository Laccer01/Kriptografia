from lab2 import encrypt_basic, decrypt_basic

deck = [];
for i in range(1,55):
    deck.append(i);


deck1 = [];
for i in range(1,55):
    deck1.append(i);

x1= (encrypt_basic("Solitaire", deck,"se distinge"))
print (x1)

print (decrypt_basic("Solitaire", deck1, x1))

