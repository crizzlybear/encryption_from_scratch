#===============================================================================
'''
toBinary.py

PURPOSE: For Conversions involving binary
REFERENCE: 
Functions are modified from toBinary.py from DES
'''
#===============================================================================
import math
#-------------------------------------------------------------------------------
#intToBinary(int):string 
    #Purpose: Takes num, returns binary (str) with no fixed length
    #Author: Modified my an existing function to now convert to binary of any length
    #Reference: 
        #For length of binary = log2(n)+1
        #https://math.stackexchange.com/questions/1508902/given-a-number-how-to-find-the-length-of-its-binary-representation
#-------------------------------------------------------------------------------
def intToBinary(num):
    binaryStr = ''
    #print(ch)
    binLen = math.floor(math.log2(num)+1)
    for n in range(binLen,0,-1):
        if((2**(n-1))>num):
            binaryStr+="0"
        else:
            num = num-(2**(n-1))
            binaryStr+="1"
    return binaryStr

