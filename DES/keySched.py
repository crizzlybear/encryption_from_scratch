#keySched
from toBinary import *
from toBlocks import *
from permute import *
#ASK KEY FROM USER

#first permuted choice PC1 table
PC1 = [57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4]

#Permute PC2 to use in combineCD
PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]
#GENERATE SUBKEYS ===========
#---------------------------------------------------------------
#generateSubKeys(string): string list
"""
    1. Binary string len 64 > Permute with PC1 -> len 56
    2. Split in half: C (28 bits) and D (28 bits)
    3. Rotate C and D each 16 rounds
    4. Combine list of C and list of D into CD list
    5. Permute CD list with PC2 -> len 48
    6. return subkey list
"""
#---------------------------------------------------------------
def generateSubKeys(inStr):#Input needs to be in binary string of 64 bits, PC1 removes 8 bits making it total 56bits
    #bits 8, 16, 24, 32, 40, 48, 58, 64 are removed
    #print("input",inStr)
    #print(len(inStr))
    if(len(inStr)!=64):
        print("Error: keySched.py: generateSubKeys() input is not 64 bits in length:", inStr, "len:",len(inStr))
    kPC1 = permute(inStr, PC1)
    #print("!PC1:", kPC1)
    #print(len(kPC1))
    #split into half
    C = kPC1[slice(0,28)] #subkey
    #print("C",C)
    D = kPC1[slice(28,56)]
    #print("D",D)
    #rotate sk1 and sk2 accordingly
    CList = rotate16(C)
    DList = rotate16(D)
    CnDnList = combineCD(CList, DList)
    subkeys = permuteList(CnDnList, PC2)
    return subkeys


#---------------------------------------------------------------
#shiftL(string, int): string
#   Purpose: shifts left n bits
#   Input: binary string len 28
#   Returns: binary string len 28
#---------------------------------------------------------------
def shiftL(binStr, n):
    size = len(binStr)
    new = binStr[n:] + binStr[0:n]
    return new

#---------------------------------------------------------------
#rotate16(string): string list
#   purpose: takes binary string and rotates 16 rounds (28 times)
#   Input: binary string len 28
#   Returns: binary string len 28
#---------------------------------------------------------------
def rotate16(R):
    Rlist = []
    rotate1 = [1,2,9,16]#round2rotate
    for r in range(1,17): #1-16
        if(r in rotate1):
            #rotate once
            R = shiftL(R,1)
            Rlist.append(R)
            
        else:
            #rotate twice
            R = shiftL(R,2)
            Rlist.append(R)
    return Rlist
"""
#TEST rotate16
#if it works, after 16 rounds (28 total rotations, the 1 will return to original location
s = "1000000000000000000000000000"
print("rotate16")
print(rotate16(s))
"""
#---------------------------------------------------------------
#combineCD(string list, string list): string list
#   Purpose: combine corresponding elements of each list
#           Used in generateSubKeys()
#   Input: 2 string (len 28) lists 
#   Returns: string (len 56) list
#---------------------------------------------------------------
def combineCD(Clist,Dlist):
    #Kn = CnDn where n = index +1
    #so Clist[0] and Dlist[0] = C1D1
    CnDn = []
    for i in range(0,16): #0-16
        CnDn.append(Clist[i] + Dlist[i])
    return CnDn

#---------------------------------------------------------------
#permuteList(string list, list):
#   Purpose: iterates through list and permutes with table
#           Used in generateSubKeys()
#   Input: binary string (len 56) list
#           table name
#   Return: string (len 48) list 
#---------------------------------------------------------------
def permuteList(strList, table):
    pList = []
    for i in strList:
        pList.append(permute(i,table))
    return pList

##TESTING##
"""
k = "1111111011111110111111101111111011111110111111101111111011111110"
#PC1 shoudl remove the 0s
myKeys = generateSubKeys(k)
for sk in myKeys:
    print(sk, len(sk))#should b 48bits
"""


