#============================================================================
'''
rsa_decrypt.py

PURPOSE: (Simulate encrypted communication from Alice to Bob)
    >BOB (this) reads cipher, performs decoding, decryptes message using
    public and private keys    
    >Run in 'main'

REFERENCE:
    RSA implementation examples
    https://www.uobabylon.edu.iq/eprints/paper_1_17152_649.pdf
'''
#============================================================================
from .readfile import *
from .binModExp import *
from .toHexa import *
from .blocks import *
#--------------------------------------------------------------------------
#RSAdecrypt():
    #Purpose: reads ciphertext (assumes exists so it is hardcoded), 
        #splits and decodes, then decrypts using 
        #m = c^d mod n to retrieve plaintext
        #displays plaintext in terminal
#--------------------------------------------------------------------------
def RSAdecrypt():
    mList = []
    #readfile into string,
    #inStr = list(readToString("cipher.txt"))
    inStr = readToString("cipher.txt")
    #get public key
    kPub = readToString("public_key.txt")
    x = kPub.split(",")
    #get private key
    kPr = readToString("private_key.txt")
    n = int(x[0])
    e = int(x[1])
    d = int(kPr)
    
    msgBlocks = []
    cipherBlocks = inStr.split(" ")#cipher blocks separated by spaces
    for cipher in cipherBlocks:#source decode
        dec = hexToDec(cipher)
        #decrypt
        mDec = binModExp(dec,d,n)
        hexa = list(intToHex(mDec))
        char=""
        while(len(hexa)>1):
            h=hexa.pop(0)
            h+=hexa.pop(0)
            hInt = hexToInt(h)
            char += chr(hInt)
        msgBlocks.append(char)
    print("".join(msgBlocks))
        
#=====main======   
# RSAdecrypt()
