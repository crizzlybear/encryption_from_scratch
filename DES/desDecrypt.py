from fFunc import*
from sBox import *
from readfile import *
from keySched import *
from toBinary import *
from feistelNet import *
from toHexa import *


"""
RUN PROGRAM
0. Ask user for file, key
1. Initial Permutation
2. Key generation
3. Feistel network round 1-16
4. Final Permutation
"""
IP = IP()
IPinv = IPinv()

#====================================================
#Get cipher from file
#Put into list length 64
#====================================================
hexCipher = readToString("desOutput.txt")
asciiCipher = hexToAsciiString(hexCipher)
cipher = toBinaryBlocks(asciiCipher)

#=====================================================
#Get Key from user
#Generate subkeys again
#=====================================================
# userInput = input("Enter key:")
# binaryInput = ""
# for c in userInput:
#     binaryInput += toBinary(c)
# #check len, binaryInput should be 64 bits in length
# if(len(binaryInput)<64):
#     print("padding key...")
#     binaryInput+=(64-len(binaryInput))*("0")
# else:
#     print("trimming key")
#     binaryInput[0:64]
# subKeys = generateSubKeys(binaryInput)#returns list


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
print("KEY (Use this to decrypt):", userInput)
binaryInput = ""
for c in userInput:
    binaryInput += toBinary(c)
#print("64 bit key binary ", binaryInput)
subKeys = generateSubKeys(binaryInput)#returns list
#print("Subkeys",subKeys)


#=====================================================
                    #DECRYPT
#Same process as encrypt except subkey order is reversed
#=====================================================
#print(len(cipher))
mText = []
for cc in cipher:
    #1. IP
    cIP = permute(cc, IP)
    #print("block permuted", cIP)
    #2. feistel rounds
    for sk in reversed(subKeys):#16 subkeys
        cIP = feistelRound(cIP,sk)
        #print("round",mIP)
    #after round 16, L16 and R16 swap
    half = len(cIP)//2
    R16 = cIP[0:half] 
    L16 = cIP[half:len(cIP)]
    #3. Final Permutation
    LR16 = L16+R16
    #print("LR16",LR16)
    m = permute(LR16,IPinv)
    #print("IP-1",m)
    mText.append(m)
#=============================================================
#Text processing
#Convert from binary to ascii
#Ask user if padding needs to be removed
#=============================================================
#convert cText to ascii
decrypted = "".join(mText)
#print("DECRYTPED",decrypted)
decryptedText = binToAscii(decrypted)
print("Decrypted Text:", decryptedText)
#>Remove padding form decrypted text
ans = input("Remove padding from decrypted text? (Y/N)").upper()
i=-1
while(i==-1):
    if(ans == "Y"):
        i=1
        print(removePadding(decryptedText))
    elif(ans == "N"):
        i=0
        print("done")
    else:
        ans = input("Remove padding from decrypted text? (Y/N)").upper()
        i=-1






