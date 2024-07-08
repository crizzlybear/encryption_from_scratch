#f function
"""
1. expansion E #same as permute
2. XOR with round key
3. S box sub in Sbox.py
4. permutation
"""
from permute import *
from sBox import *
#E bit table =======================
E = [32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25, 
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1]
    
    #use permute(inStr, E)

#----------------------------------------------------
#XOR 
#XORkey(string, string): string
#   Purpose: xor 2 binary strings of same length
#   Input: 2 binary strings (so long they are of same length)
#   Output: binary string
#----------------------------------------------------
def XORkey(inStr, sk): #sk = subkey
    xored = ""
    if(len(inStr)!=len(sk)):
        print("ERROR: XORkey()-cannot xor, not the same length")
    else:
        for i in range(0,len(inStr)):
            xored += str(int(inStr[i])^int(sk[i]))
    return xored
'''
a = "1111"
b = "1101"
c = XORkey(a,b)
print(a,b,c)
'''
#----------------------------------------------------
#FFUNCTION
#fFunction(string, string): string
#   Purpose: Perform f function on R0 and subkey
#   Input: R0 string (len 32)
#       subkey string (len 48)
#   Returns: string
#----------------------------------------------------
#putting it all togther
P = [16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25]

def fFunction(R0, subKey):
    R = permute(R0, E)
    #print("!R perm E", R)
    s48 = XORkey(R, subKey)
    #print("!RxorK", s48)
    s32 = sBox8(s48)
    #print("!sBox", s32, len(s32))
    #print("!!", len(P)*8)
    fOut = permute(s32, P)
    return fOut
"""
#TESTING
inStr = "00000000011111101000000000001101" #len 32
k = "00000011001011100010001100110000"
print(fFunction(inStr, k))
#exp = "10010111010111001001000011001101"
#WORKS!
"""


