#HEX CONVERSIONS
#if we want tp use as a int to hex, then remove ch=ord(str(ch))
#------------------------------------------------------------
#toHex(char):string
#   Purpose: convert character len 1 to hexa value
#   Input: character len 1, int also works if single digit
#   Return: hex value string (len 2)
#------------------------------------------------------------
def toHex(ch):
    """
    if(type(ch)!=int):
        ch = ord(ch)
    """
    ch = ord(str(ch))
    hexStr = ""
    while((ch//16)!=ch):
        #print(ch, ch//16, ch%16)
        r = ch%16
        if(r >9):
            l =((r%10))+65
            hexStr+=chr(l)
        else:
            hexStr+=(str(r))
        ch = ch//16
    hexStrRev = hexStr[::-1]
    return hexStrRev

"""
a = toHex('a')
b = toHex('b')
n3 = toHex(3)
a3 = toHex('3')
sE = toHex('!')
sHash = toHex('#')
print('a',a)
print('b',b)
print('3',n3)
print('ascii 3', a3)
print('!',sE)
print('#',sHash)
print('l',toHex('l'))
#print('16',toHex(16)) should be invalid
#print(16/16, 1//16)
"""
#------------------------------------------------------------
#hexToAscii(string): char
#   Purpose: Convert hex value to ascii char
#       used in hexToAsciiString()
#   Input: hex value (len 2)
#   Return: char len 1
#------------------------------------------------------------
def hexToAscii(inStr):
    assert(len(inStr)%2==0) #"hexToAscii(): value entered is not hexadecimal (length needs to be 2)"
    inStr.upper()
    #inStr is an hex value of 2 characters e.g. 33  = '3', 6C = 'l', 61 = 'a'
    hexConversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    i1 = hexConversion.index(inStr[0])
    i2 = hexConversion.index(inStr[1])
    n = i1*16 + i2*1
    #print(chr(n))
    return chr(n)

#print(hexToAscii("23"))

#------------------------------------------------------------
#hexToAsciiString(string): string
#   Purpose: convert hex string to ascii string
#   Input: hexadec string
#   Return: ascii string
#------------------------------------------------------------
def hexToAsciiString(inStr):
    #takes hexa string
    n=0
    temp = ""
    asciiStr = ""
    for h in inStr:
        temp += h 
        n+=1
        if(n==2):
            asciiStr+=hexToAscii(temp)
            n=0
            temp = ""
    assert(temp=="") #"error in hexToAscii(), hex string entered is wrong, each hex value needs to be len 2"
    return asciiStr

#print(hexToAsciiString("6C33616223"), "|exp = l3ab#")

