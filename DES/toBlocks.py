"""
PURPOSE: Padding and creating blocks of 64 bits 
NOTES
ansi characters 32-126
"""
import random
from toBinary import *
from toHexa import toHex
#------------------------------------------------------------
#n2Pad(string):int
#   Purpose: Used in paddingR(). Returns number of characters
#   to pad the input string (ascii)
#   Input: ascii string
#   Returns: number of characters to pad
#------------------------------------------------------------
def n2Pad(inStr):
    if(len(inStr)%8==0):
        char2Pad = 0
    else:
        char2Pad = 8-(len(inStr)%8)
    return char2Pad
#------------------------------------------------------------
#paddingR(string): string
#   Purpose: Pad the input string(ascii) with random
#   ascii characters to the value of n2Pad(). The last
#   padded character is n2Pad()
#   Input: ascii string
#   Returns: ascii string
#------------------------------------------------------------
def paddingR(inStr):
    n = n2Pad(inStr)
    expStr = ""
    if(n == 0):
        expStr = inStr
    elif(n==1):
        expStr = inStr + str(n)
    else:
        randomString = ""
        for r in range(0, n-1):
            randomString += chr(random.randint(32,126))
        expStr = inStr + randomString + str(n) 
    return expStr

#TESTING
#print(paddingR("hello"), n2Pad("hello"))

#------------------------------------------------------------
#removePadding(string): string
#   Purpose: Remove padding, gets last char, if a number, then
#   remove the same number of characters
#   Input: ascii string
#   Returns: ascii string
#------------------------------------------------------------
def removePadding(inStr):
    #USE AFTER DECRYPTiNG
    #where inStr is the decrypted text
    n = ["1", "2", "3", "4", "5", "6", "7"]
    lastCh = inStr[len(inStr)-1]
    try:
        charToRemove = n.index(lastCh)+1
        endIndex = len(inStr)-charToRemove
    except:
        endIndex = len(inStr)
    return inStr[0:endIndex]

#TESTING
#print("WORD**3",removePadding("WORD**3"))
#print("WORD",removePadding("WORD"))
    
#------------------------------------------------------------
#toBinaryBlocks(string): string List
#   Purpose: Take a striing of ascii characters, converts to
#   binary, and splits into a list of 64 bits
#   Input: ascii string
#   Returns: list of binary string (length 64)
#------------------------------------------------------------
def toBinaryBlocks(inStr): #makes blocks of 8 chars, then converts to binary
    blocks = []
    char8 = ""
    bblocks = []
    for c in inStr: 
        char8+=c
        if(len(char8) == 8):
            blocks.append(char8)
            char8 = ""
    for m in blocks:
        bblocks.append(stringToBinary(m))
    return bblocks

#------------------------------------------------------------
#binaryBlocks2HexBlocks(string):string
#   Purpose: Converts binary list to hexadecimal list
#   Input: List of binary strings
#   Returns: List of hexadecimal strings
#------------------------------------------------------------
def binaryBlocks2HexBlocks(binList):
    hexList = []
    for b in binList:
        hexList.append(binToHexa(b))
    return hexList
"""
#TESTING
inStr = "hello world"
print("ORIGINAL", inStr, "bits", len(inStr)*8)
expandStr = paddingR(inStr)
print(expandStr)
bb = toBinaryBlocks(expandStr)
print(bb)
hh = binaryBlocks2HexBlocks(bb)
print(hh)
"""
