#============================================================================
'''
rsa_encrypt.py

PURPOSE: (Simulate encrypted communication from Alice to Bob)
    >ALICE encrypts message using public key from BOB
    >Ciphertext is written to file (in hexadecimal format)
    >Run in 'main'

REFERENCE:
    RSA implementation examples
    https://www.uobabylon.edu.iq/eprints/paper_1_17152_649.pdf
'''
#============================================================================
from readfile import *
from binModExp import *
from toHexa import *
from blocks import *
from keySchedule import *

#---------------------------------------------------------------------------
#RSAencrypt(string):
    #Purpose: Open a plaintext file, Open public key, Perform source coding
        #Encrypt using c = m^e mod n
        #Write cipher to file (hex blocks separated by space)
#---------------------------------------------------------------------------
def RSAencrypt(filename):
    #f = open(filename)
    inStr = readToString(filename)#enter messgae to encrypt
    #from public key:
    kPub = readToString("public_key.txt")
    x = kPub.split(",")
    try:
        n = int(x[0])
        e = int(x[1])
    except:
        print("RSA encrypt error converting kPub to n and e",x[0])
    cipherBlocks = []
    blocks = blockList(inStr)#to blocks size of 8
    for msg in blocks:#source coding
        hexa = ""
        for i in msg:
            hexa += toHex(i)
        dec = hexToDec(hexa)
        c = binModExp(dec,e,n)
        cHex = intToHex(c)
        cipherBlocks.append(cHex)
    
    cipherBlockStr = " ".join(cipherBlocks)
    writeToFile(cipherBlockStr, "cipher.txt")
    print("Cipher text written: cipher.txt")

        
#=====main======   
try:
    generateKeys()
    RSAencrypt("test4.txt")
except:
    print("Error generating private and public keys")

