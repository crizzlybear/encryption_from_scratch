#Feistel Network
from keySched import *
from fFunc import *
#------------------------------------------------------------
#feistelRound(string, string): string
#   Purpose: Performs feistel round for the given string and key
#   Input: inStr is the permuted binary string (len 64)
#           subKey is the subkey for the round (len 48)
#   Returns: string after round
#------------------------------------------------------------
def feistelRound(inStr, subKey):
    half = len(inStr)//2
    L0 = inStr[0:half]
    R0 = inStr[half:len(inStr)]
    #print("L0",L0, "|R0",R0)
    R1 = XORkey(L0, fFunction(R0, subKey))
    #print("L0 xor fFunc(R0 key1)",R1)
    L1 = R0
    outStr = L1+R1 
    return outStr
