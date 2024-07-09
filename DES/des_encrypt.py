#=======================================================
#PROGRAM TO ENCRYPT DES
#=======================================================
from .fFunc import*
from .sBox import *
from .readfile import *
from .keySched import *
from .toBinary import *
from .feistelNet import *
#from toHexa import *


"""
RUN PROGRAM
0. Ask user for file, key
1. Initial Permutation
2. Key generation
3. Feistel network round 1-16
4. Final Permutation
"""


#========================================================
#Ask user for file
#Pad message
#Put message into 64 bit list
#=======================================================
def DESencrypt():
    Ip = IP()
    IpInv = IPinv()
    fileName = input("Enter file name:")
    message = readToString(fileName)
    if(len(message)%8!=0):
        print("Padding message...", len(message))
        messagePadded= paddingR(message)
    else:
        messagePadded = message
    # print("message padded:",messagePadded)
    message64 = toBinaryBlocks(messagePadded) #returns a list
    #print("messageBlocks:", message64)

    #========================================================
    #Ask user for key
    #Generate subkeys
    #=========================================================

    userInput = input("Enter key:")
    if(len(userInput)<64):
        #userInput = paddingR(userInput) #if the key is too short, it will add random chars to make up the required len. You have to copy this and use to decrypt
        userInput += (64-len(userInput))*("0")
        print("key is less than 64 bits:", len(userInput)*8, "padding key...")
    elif(len(userInput)>64):
        userInput = userInput[0:64]
        print("key is more than 64 bits:", len(userInput)*8, "cutting key...")
    #if 64 continue
    #Make subkeys
    #userInput to binary
    # print("KEY (Use this to decrypt):", userInput)
    binaryInput = ""
    for c in userInput:
        binaryInput += toBinary(c)
    #print("64 bit key binary ", binaryInput)
    subKeys = generateSubKeys(binaryInput)#returns list
    #print("Subkeys",subKeys)
    #===========================================================
                            #ENCRYPTION
    #Permute IP
    #Feistel rounds
    #Permute IPinverse
    #===========================================================

    cText = []
    for m in message64:
        #1. IP
        mIP = permute(m, Ip)
        #print("block permuted", mIP)
        #2. feistel rounds
        for sk in subKeys:#16 subkeys
            mIP = feistelRound(mIP,sk)
            #print("round",mIP)
        #after round 16, L16 and R16 swap
        half = len(mIP)//2
        R16 = mIP[0:half] 
        L16 = mIP[half:len(mIP)]
        #3. Final Permutation
        LR16 = L16+R16
        #print("LR16",LR16)
        c = permute(LR16,IpInv)
        #print("IP-1",c)
        cText.append(c)
    #==============================================================
    #Process encrypted text
    #Convert to hexadecimal
    #Write encrypted to file C.txt
    #==============================================================
    #encrypted is in binary
    encrypted = "".join(cText)
    #print("Encrypted message in binary:",encrypted)
    #convert encrypted to hex
    encryptedHex = binToHexa(encrypted)
    print("Encrypted message in hex:",encryptedHex)
    writeToFile(encryptedHex, "desOutput.txt")
    print("File C.txt created and written")

