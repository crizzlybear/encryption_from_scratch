#==============================================================================
'''
PURPOSE: Conversions involving Hexadecimal
REFERENCE: Modified functions from toHexa.py from DES
'''
#==============================================================================
#-----------------------------------------------------------------------------
#toHex(char):string
   #Purpose: convert character len 1 to hexa value
   #Input: character len 1, int also works if single digit
   #Return: hex value string (len 2)
   #Reference: Previous submission
#----------------------------------------------------------------------------
def toHex(ch):
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

#-=======================================================================
#*MODIFIED*
#intToHex(int):string
    #Purpose: Converts (decimal)int to hexadecimal
    #Reference: modified toHex() from previous submission
#=========================================================================
def intToHex(n):
    
    if(n<=9):
        ans = "0"+str(n)
    elif(n>=10 and n<=15):
        letter = ["0A","0B","0C","0D","0E","0F"]
        i = n-10
        ans = letter[i]
    else:
        hexStr = ""
        while((n//16)!=n):
            #print(ch, ch//16, ch%16)
            r = n%16
            if(r >9):
                l =((r%10))+65
                hexStr+=chr(l)
            else:
                hexStr+=(str(r))
            n = n//16
        hexStrRev = hexStr[::-1]
        ans = hexStrRev
    return ans
'''
print("int to hex TESTING::")
print(intToHex(97))#ans = 61
print(intToHex(93))#ans = 5D
'''
#=========================================================================
#NEW modified hexToAscii()->now returns int
#hexToInt(string):int
    #Purpose: Converts hex to int (but only accepts 1 byte hex 00-FF)
    #Reference: Previous submission
#=========================================================================
def hexToInt(inStr): #technically hex to decimal int
    assert(len(inStr)%2==0) #"hexToAscii(): value entered is not hexadecimal (length needs to be 2)"
    inStr.upper()
    #inStr is an hex value of 2 characters e.g. 33  = '3', 6C = 'l', 61 = 'a'
    hexConversion = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    i1 = hexConversion.index(inStr[0])
    i2 = hexConversion.index(inStr[1])
    n = i1*16 + i2*1
    #print(chr(n))
    return ord(chr(n))
'''
print("testing HexToInt()")
print(hexToInt("23"))#ans = 35
print(hexToInt("5D"))#ans = 93
'''
#========================================================================
#hexToDec(string): int
    #Purpose: convert hex to dec int (similar to hexToInt() but takes valuea
    #larger than 1 byte
    #Reference:
        #Conversion table
        #https://www.rapidtables.com/convert/number/hex-to-decimal.html
#========================================================================
def hexToDec(hexStr):
    arr = []
    dec = 0
    letters = ['A','B','C','D','E','F']
    counter = len(hexStr)-1
    for i in hexStr:
        #print("hexa",i,ord(i))
        if(ord(i)>=48 and ord(i)<=57):
            #print(i,"is a number", counter)
            dec += int(i) * pow(16,counter)
        else:
            #print(i,"is a letter", counter)
            n = letters.index(i) + 10
            dec += n * pow(16,counter)
        counter = counter-1
    return(dec)
