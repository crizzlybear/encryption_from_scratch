#------------------------------------------------------------------------
#readToString(string): string
#   Purpose: opens and reads file. Stores contents into string
#   Input: string file name
#   Return: string
#------------------------------------------------------------------------
def readToString(inputFile):
    try:
        f = open(inputFile,"r")
        inStr = ""
        for line in f.readlines():
            inStr += line
            #print(line)
    except IOError: #IOError is OSError in py3, OS when file does not exist
        print("Error opening file: file not valid or file does not exist")
    except:
        print("Unexpected error")
    return inStr
"""
    inStr = ""
    inStr = f.readline().strip()
    return inStr
"""

#----
#print(readToString("DES-test.txt"))
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

