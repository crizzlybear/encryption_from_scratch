#CONVERSIONS

#-------------------------------------------------------------
#toBinary(string):string
#   Purpose: Convert char (len 1)  to binary (len 8)
#   Input:takes char (and numbers as a string), returns string
#   Returns: 8 bit binary string
#--------------------------------------------------------------
def toBinary(ch):
    ch = ord(str(ch))
    binaryStr = ''
    #print(ch)
    for n in range(8,0,-1):
       # print(n)
        if((2**(n-1))>ch):
            binaryStr+="0"
        else:
            #print(ch-(2**n))
            ch = ch-(2**(n-1))
            binaryStr+="1"
    return binaryStr      

#for Values less than 255
#fine for ascii since they are all 8 bit
"""
a = toBinary('a')
b = toBinary('b')
n3 = toBinary(3)
sE = toBinary('!')
sH = toBinary('#')
print('a', a)
print('b', b)
print('3', n3)
print('!', sE)
print('#', sH)
"""
#-------------------------------------------------------------
#intToBinary(int): string
#   Purpose: in sBox
#       Converts int upto value 0-15 to 4 bit binary
#   Input: number 0-15
#   Returns: binary string len 4
#-------------------------------------------------------------
def intToBinary(num):
    #UPT0 15 since more will exceed len 4 1111
    binaryStr = ''
    #print(ch)
    for n in range(8,0,-1):
       # print(n)
        if((2**(n-1))>num):
            binaryStr+="0"
        else:
            #print(ch-(2**n))
            num = num-(2**(n-1))
            binaryStr+="1"
    return binaryStr[4:8]      

#-------------------------------------------------------------
#binToAscii(string):string
#   Purpose: Convert binary (len = multiple of 8) to ascii string
#   Input: binary string 
#   Return: ascii string
#-------------------------------------------------------------
def binToAscii(inStr):
    #takes binary string
    n = 0
    power = 7
    dec = 0 #decimal to later convert to ascii using ch()
    asciiList = []
    for b in inStr:
        dec += int(b)*(2**(power-n))
        n+=1
        #print(dec, n)
        if(n==8):
            #print(dec)#exp 119, 111, 114, 110
            asciiList.append(chr(dec))
            n=0
            dec = 0
    return "".join(asciiList)   

#Testing  
#print("01110111011011110111001001100100->", binToAscii("01110111011011110111001001100100"), "|exp = word")


#-------------------------------------------------------------
#binToHexa(string): string
#   Purpose: Convert binary string to hexa
#   Input: binary string (len = multiple of 4)
#   Returns: string of hexadecimal
#-------------------------------------------------------------
#https://www.tutorialspoint.com/how-to-convert-binary-to-hexadecimal
def binToHexa(inStr):
    #Works with multiples of 4 only, otherwise will be wrong
    #Used at the end of encryption so it should be a multple of 4
    #takes binary string
    if(len(inStr)%4 != 0):
        print("binToHexa(): input is not a multiple of 4")
    bin4 = ["0000","0001", "0010", "0011", "0100", "0101", "0110", "0111", 
            "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
    hexVal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
            "A", "B", "C", "D", "E", "F"]
    n = 0
    power = 7
    hexa = "" #decimal to later convert to ascii using ch()
    hexaList = []
    for b in inStr:
        hexa += b
        n+=1
        #print(dec, n)
        if(n==4):
            #print(dec)#exp 119, 111, 114, 110
            index = bin4.index(hexa)
            h = hexVal[index]
            hexaList.append(h)
            n=0
            hexa = ""
    return "".join(hexaList)
#print(binToHexa("111100001110"))

#-------------------------------------------------------------
#stringTobinary(string): string
#   Purpose: Convert string to binary
#   Input: ascii string
#   Return: binary string
#-------------------------------------------------------------
def stringToBinary(inStr):
    n = 0
    bStr = ""
    binaryList = []
    for c in inStr:
        n+=1
        #print(dec, n)
        bStr += toBinary(c)
    return bStr
#print(stringToBinary("hello"))
