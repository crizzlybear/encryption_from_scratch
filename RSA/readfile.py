#========================================================================
'''
readfile.py
PURPOSE: Read and write to file functions
REFERENCE:
    (MODIFIED) Previously submitted readfile.py in DES
    #Removed: for line in f.readlines()
    #replace with for l in f In Python 3, 
    to prevent print prints trailing newline, you can use print(i, end='').
    #actually just remove trailing newline using iStr = inStr.rstrip('\n')
'''
#=========================================================================

#------------------------------------------------------------------------
#readToString(string): string
#   Purpose: opens and reads file. Stores contents into string
#   Input: string file name
#   Return: string
#------------------------------------------------------------------------
def readToString(inputFile):
    inStr = ""
    try:
        f = open(inputFile,"r")
        for l in f:
            inStr +=l        
        
    except IOError: #IOError is OSError in py3, OS when file does not exist
        print("Error opening file: file not valid or file does not exist")
    except:
        print("Unexpected error")
    inStr = inStr.rstrip('\n')
    return inStr

#------------------------------------------------------------------------
#writeToFile(string, string): string
#   Purpose: Opens file and writes string
#   Input: string to write, 
#           filename
#   Returns: string to write
#------------------------------------------------------------------------
def writeToFile(inStr, fileName):
    try:
        f = open(fileName,"w")
    except:
        print("Unexpected error opening/creating file")
    f.write(inStr)
    f.close()
    return inStr

