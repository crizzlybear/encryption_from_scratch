#===================================================================
'''
binModExp.py

PURPOSE: Perform fast exponential calculations (with or without mod)
    Alternative to pow(n,e,m) n^e mod m
'''
#===================================================================
from toBinary import *
#-------------------------------------------------------------------
#binModExp(int,int,int(optional)):int
    #Purpose: Use instead of pow(n,e,m) = n^e mod m 
    #Reference:
        #Optional python param like pow(n,e) and pow(n,e,m)
        #https://stackoverflow.com/questions/41745001/use-default-argument-if-argument-is-none-on-python-method-call
#-------------------------------------------------------------------
def binModExp(n,e,m = None):
    #eBin = toBinary(e) #list of binary
    eBin = list(intToBinary(e))#intToBinary() returns string
    ans = n
    if(m is not None):
        for i in range(1,len(eBin)):
            ans = pow(ans,2)%m
            if int(eBin[i]) == 1:
                ans = (ans*n)%m
    else:
        for i in range(1,len(eBin)):
            ans = pow(ans,2)
            if int(eBin[i]) == 1:
                ans = (ans*n)
    return ans
'''
print(pow(4,37,68))
print(binModExp(4,37,68))
'''
