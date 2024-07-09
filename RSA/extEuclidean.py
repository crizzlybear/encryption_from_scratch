#============================================================================
'''
extEuclidean.py
PURPOSE: Use extended euclidean algorithm to calculate modular inverse and gcd
REFERENCE:
    The code for the algorithm was based on an example calculation
    http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
'''
#============================================================================
#----------------------------------------------------------------------------
#inverseMod(int,int):int
    #Purpose: Iteratively find mod inv. At the last 0 remainder, then a 
    #has an inverse (pn).
#----------------------------------------------------------------------------
def inverseMod(a,m):
    #CALCULATE MODULAR INVERSE of a. where m is modulus
    a0=a
    m0=m
    r = -1
    i = 0
    p=0
    xArray = []
    rArray = []
    #m = ax+r
    while(r!=0):
        r = m%a
        x = (m-r)//a
        m = a
        a = r
        xArray.append(x)
        rArray.append(r)
    if(len(xArray) != 0):
        p0=0
        p1=1
        xArray.pop()
        for i in xArray:
            pn = (p0-p1*(i))%m0
            p0= p1
            p1=pn
    return pn#will throw error if invalid (ie when  gcd(a,m)!=1) 
#----------------------------------------------------------------------------
#GCD(int,int):int
    #Purpose: Returns greatest common div. Found that I could use r from 
    #the algorithm to find GCD
#----------------------------------------------------------------------------
def GCD(a,m):
    a0=a
    m0=m
    r = -1
    i = 0
    p=0
    rArray = []
    #m = ax+r
    while(r!=0):
        r = m%a
        x = (m-r)//a
        m = a
        a = r
        rArray.append(r)
    if(m0%a0==0):
        #print("gcd = ",a0)
        gcd = a0
    elif(1 not in rArray): #checks gcd = 1, if it's not 1: then there is no mod inverse
        #print("gcd = ", rArray[-2])#gcd before remainder 0
        gcd=rArray[-2]
    else:
        gcd=1
    return gcd

##TESTING
'''
x = inverseMod(3,26)
print(x)
print(GCD(30,18))
#inverseMod(x,27)
'''
