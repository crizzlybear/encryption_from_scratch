#ref: https://www.dcode.fr/affine-cipher
#TEST:
#python3 AffineDecrypt.py | grep -E --color -i "wordtofind"

#15/04/22 is working
#Answer: A inverse = 9, b = 9
#gives key a = 3, b = 9
#METHODS----------------------------------------------------
#Read one line of file: 
#-Takes filename
#-Returns first line of file 
#TODO: make a function for calculating inverse mod instead of array
#----------------------------------------------------------
def readToString(inputFile):
    try:
        f = open(inputFile,"r")
    except IOError: #IOError is OSError in py3, OS when file does not exist
        print("Error opening file: file not valid or file does not exist")
    except:
        print("Unexpected error")

    inStr = ""
    inStr = f.readline().rstrip().lower()
    #print("original string", inStr)
    return inStr
#-----------------------------------------------------------
#Read whole file. Iterates through each line, decrypting it using decryptLine().
#-Takes filename
#-Returns decrypted text
#-key a and b need to be defined first otherwise this method will not work
#----------------------------------------------------------
def readAll(inputFile,aIkey, bKey):
    try:
        f = open(inputFile,"r")
    except IOError: #IOError is OSError in py3, OS when file does not exist
        print("Error opening file: file not valid or file does not exist")
    except:
        print("Unexpected error")

    inStr = ""
    for line in f:
        temp = line.rstrip().lower()
        temp = decryptLine(temp, aIkey, bKey)
        inStr += temp+"\n"
        #print(temp,'\n')
    return inStr
   #print(inStr)
#-------------------------------------------------------------
#Decrypt line. Decrypts only lower case characters, symbols are unmodified since in the ciphertext they are visible.
#-Takes temp(aka line from file)
#-Returns decrypted line
#-Used in readAll()
#-------------------------------------------------------------
def decryptLine(temp, aIkey, bKey):
    original = []
    for i in temp:
        #print("i", i) 
        #does not decyrpt symbols, only letters
        if((ord(i)<=64 and ord(i)>=32)or (ord(i)<=96 and ord(i)>=91) or (ord(i)<=126 and ord(i)>=123)):
            original.append(i)
        else:
        #letter c
            c = ord(i)-97
    #set a and b
    #decrypt = (aI*(abs(b-c)))%26
            decrypt = (int(aIkey)*(c-int(bKey)))%26
            
            original.append(chr(decrypt+97))
    return ''.join(original)


#===========================================================================
#                       AFFINE DECRYPT PROGRAM
#===========================================================================
#Get file name
def affine(inputFile):
    #== A and A INVERSE VALUES==
    a = [1,3,5,7,9,11,15,17,19,21,23,25]
    #let b = range 0-26
    aInverse = [1,9,21,15,3,19,7,23,11,5,17,25]
    #inputFile = input("Enter file name: ")
    cipher = readToString(inputFile)
    #==BRUTE FORCE==
    #--Iterate though all combinations of a inverse and b to decrypt 1 line of the text.
    #--The user needs to manually find the line that gives plaintext
    #--assume you dont know a and b
    #--decrypt = (aInverse)*(c-b)mod26
    #--c = cipher text
    print("rotations             InverseKey, bKey")
    print("_______________________")
    original = []
    for aI in aInverse:
        for b in range(0,26):
            
            for i in cipher:
                if(ord(i)==32):
                    original.append(" ")
                else:
            #letter c
                    c = ord(i)-97
            #apply aI and b
                    decrypt = (aI*(c-b))%26
                    original.append(chr(decrypt+97))
            print(''.join(original),'          >', aI, b)
            original = []
    #==GET KEY==
    #--User needs to input the a inverse and b that gave the plaintext
    #--returns corresponding a value in the final key
    aIKey = input("Enter a inverse:")
    print("aiKey", aIKey)
    bKey = input("Enter b:")
    
   
    print("_______________________")
    #==DECRYPT FULL TEXT WITH KEY==
    print("Decrypting with key... AI")
    print(readAll(inputFile, aIKey, bKey))
    #convert aI to a
    indexA = aInverse.index(int(aIKey))
    aKey = a[indexA]
    print("_______________________")
    print("Original encryption KEY was a:",aKey,"b:", bKey)
    print("Decryption key aI:",aIKey," -> aKey:",aKey, "\n")
    #--------------------
