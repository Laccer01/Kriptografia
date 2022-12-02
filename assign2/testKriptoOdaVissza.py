from lab2 import *



def beolvasEncryptalas():
    configFile = open("config", "r")
    dataFromFile = configFile.read().splitlines()
    dataFromFile[1] = int(dataFromFile[1])
    if(len(dataFromFile)>2):
        dataFromFile[2] = int(dataFromFile[2])

    return dataFromFile;

dataFromFile = beolvasEncryptalas();
# s,n = generateSandN();

# print (encrypName)
# print ("Blum_Blum_Shub")
# print (encrypName == "Blum_Blum_Shub")
# print (len(encrypName))
# print (len("Blum-Blum-Shub"))
x1= (encrypt_basic(dataFromFile[0],dataFromFile[1],"mano",dataFromFile[2]))
print (x1)
print (decrypt_basic(dataFromFile[0],dataFromFile[1],x1,dataFromFile[2]))

