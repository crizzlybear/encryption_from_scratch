#====================================================================
'''
blocks.py

PURPOSE: helper function for RSAencrypt and RSAdecrypt
    Splits string into blocks of 8 char (including remaining chars)
'''
#====================================================================
#--------------------------------------------------------------------
#blockList(string): stringList
    #Purpose: Splits into 8 char blocks, leaves the remaining char at 
        #the end
    #Reference:
        #Escape char handling
        #https://stackoverflow.com/questions/25047976/split-a-string-by-backslash-in-python
#--------------------------------------------------------------------
def blockList(inStr1):
    inStr = repr(inStr1)
    blocks = []
    length = len(inStr)
    if(length<8):
            blocks.append(inStr)
    else:
        #div = length - (length%8)
        #remainBlocks = inStr[div:length]
        i=0
        while(len(inStr)!=0):
            blocks.append(inStr[i:i+8])
            inStr = inStr[i+8:len(inStr)]
        #blocks.append(remainBlocks)
    return blocks
