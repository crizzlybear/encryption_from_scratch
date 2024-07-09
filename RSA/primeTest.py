#=======================================================================
'''
primeTest.py

PURPOSE: Function to test for prime (Rabin miller) and use to generate 
    large primes

REFERENCES:
    Rabin Miller Guide
    https://planetcalc.com/8995/

    A better way of implementing Rabin Miller
    https://crypto.stanford.edu/pbc/notes/numbertheory/millerrabin.html

    Rabin Miller test examples:
    http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/Rabin-Miller-Examples.pdf
    Increasing speed: (replaced with binModExp())
    https://stackoverflow.com/questions/18220278/miller-rabin-test-slow-python
NOTE: p and q need to be larger than 2^64 aka 20 digits
'''
#=======================================================================

import random
from .binModExp import *

#-----------------------------------------------------------------------
#primeTest(int): bool
    #Purpose: Check if number is a prime
    #Goes through 3 runs (probabilistic)
#-----------------------------------------------------------------------
def primeTest(p):
    #rabin miller
    #aRange = list(range(1,p-1))
    trials = 3
    aArray=[]
    n = p-1
    k=0
    l=0
    m=101#arbitrary odd number >1
    #Get k and m: n = 2^k(odd m)
    ##print("Check prime:",p)
    while(m>=1 and l>-1):#is odd
        m = n//(2**k)
        if(m%2!=0):
            ##print("m",m,"k",k)
            l=-5#arbitrary negative number less than -1
        else:
            k+=1
    a=random.randint(2,n)
    for t in range(0,trials):
        while(a in aArray):
            a = random.randint(2,n)
        aArray.append(a)
        ##print("A",a)
        #2 conditions
        cond1=False
        cond2=False
        #x=pow(a,m,p)
        x=binModExp(a,m,p)
        if(x==1 or x==-1):
            ##print("condition 1 true, probably prime")
            cond1=True
        ###
        
        for e in range(0,k):
            
            ##print("E",e,x)
            if(x-p==-1):
                ##print("condition 2 true, probably prime")
                cond2=True
                e=k+1
            #x=pow(x,2,p)
            x=binModExp(x,2,p)
        if(cond1==False and cond2==False):
            ##print("cond1 and cond2 are false")
            return False
    
    return True

#print(primeTest(89569628452852268533))
#print(primeTest(95721889))
#----------------------------------------------------------------------------
#generateLargePrime(): int
    #Purpose: Generate a prime between 2^64 and 2^100 (can be increased)
    #Use for generating p and q in keySchedule
#----------------------------------------------------------------------------
def generateLargePrime():
    #minN = pow(2,64)#len20
    #maxN = pow(2,65)
    minN = binModExp(2,64)#len20
    maxN = binModExp(2,100)#@@@@@@@@@@@@@ Can increase if needed
    prime = random.randint(minN,maxN)
    while(primeTest(prime)==False):
        prime = random.randint(minN,maxN)
    return prime

#p = generateLargePrime()
#print(p1)


