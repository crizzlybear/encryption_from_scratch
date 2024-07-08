from toBlocks import *
from toBinary import *
from toHexa import *

###INITIAL PERMUTATION and FINAL PERMUTATION==========================
#IP = initial permuation table
#changes posititions of bits
#go through IP, bit 58 (use index = 58-1) since it starts from index 1
#make empty array of 64
#these tables are global so they can be used in desEncrypt.py and desDecrypt.py
def IP():
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]
    return IP
#print(IPchange)
#------------
#FINAL PERMUT IP-1
def IPinv():
    IPinv = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
    return IPinv
#-------------------------------------------------
#permute(string, list): string
#   Purpose: permutes string with table
#   Input: Binary string
#           table name
#   Returns: permuted binary string
#-------------------------------------------------
def permute(inStr, table):
    #changed to return a string instead
    permuted = []
    tableLength = len(table)
    for n in table:
        # i = (n-1)%tableLength
        i = n-1
        permuted.append(inStr[i])
    return "".join(permuted)

##TESTING
'''
myStr = "hello world"
expStr = paddingR(myStr)
binBlock = (toBinaryBlocks(expStr))[0:64]
print(binBlock, len(binBlock))
print(len(binBlock[0]))
a = permute(binBlock[0],IP())
print(a)
b = permute(a, IPinv())
print(b)
print(binBlock[0] == b, len(b))
'''
