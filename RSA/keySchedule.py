#====================================================================
'''
keySchedule.py

PURPOSE: Generate public and private keys and write to file
    (In scenario, BOB generates the keys)
'''
#====================================================================
from .primeTest import *
from .extEuclidean import *
from .readfile import *

#--------------------------------------------------------------------
#generateKeys():
    #Purpose: Generates Kpub and Kpriv when called. Writes the keys
    #to file:
        #public_key.txt
        #private_key.txt (in real life would be a different file type)
#--------------------------------------------------------------------
def generateKeys():
    #Kpub = (n,e) and Kpr = (d) 
    Kpub = []
    #should check if they are the same...
    #also need to be the same length?
    p = generateLargePrime()
    q = generateLargePrime()
    #GENERATE PUBLIC KEY COMPONENTS: n, e
    n = p*q
    phi = (p-1)*(q-1)
    #select e
    e = random.randint(1,phi-1)#check range does it include modulus?
    while(GCD(e,phi)!=1):#CHANGED from phi-1 to phi
        e = random.randint(1,phi-1)#check range does it include modulus?
    #Public key generated...write to file
    Kpub.append(str(n))
    Kpub.append(str(e))
    Kpub_str = ",".join(Kpub)
    writeToFile(Kpub_str, "public_key.txt")
    print("public_key.txt file created.")
    
    #GENERATE PRIVATE KEY COMPONENTS: d (using e and phi)
    d = inverseMod(e,phi)
    Kpr = str(d)
    #Private key generated ... write to file
    writeToFile(Kpr, "private_key.txt")
    print("private_key.txt file created.")
###TESTING
# generateKeys()
