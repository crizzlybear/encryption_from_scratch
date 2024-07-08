#import tkinter
import string #to use string to create alpha list
import matplotlib
matplotlib.use('WebAgg')#Webbrowser GUI
import matplotlib.pyplot as plot #for plotting
#import numpy as np
#GLOBAL
alpha = list(string.ascii_lowercase) #creates list of lowercase alpha

#METHODS
#read file
def readToString(inputFile):
    try:
        f = open(inputFile,"r")
    except IOError: #IOError is OSError in py3, OS when file does not exist
        print("Error opening file: file not valid or file does not exist")
    except:
        print("Unexpected error")

    inStr = ""
    for line in f:
        #print(line.rstrip())#remove trailing new line
        temp = line.replace(" ","")#remove all whitespace
        temp = temp.replace("\n","")#remove newline
        inStr += temp
    inStr = inStr.rstrip().lower()
    #print(inStr)
    return inStr
#for a string, return freq of each letter
def getFreq(inStr):
    #alpha = list(string.ascii_lowercase) #creates list of lowercase alpha
    freq = [0]*26 #size of freq array
    for i in inStr:
        for j, letter in enumerate(alpha): #different than c
            if(i == letter):
                freq[j] +=1
    return freq
#from freq, get relative frequency
def relativeFreq(inFreq, size):
    relFreq = [0]*26
    for i, f in enumerate(inFreq):
        relFreq[i] = round((f/size),2)
        #print(i, f/size)
    return relFreq

#PROGRAM
def freq_plot(myFile):
    #myFile = input("Enter file name:") #as string
    myStr = readToString(myFile)
    strLen = len(myStr)
    #print alpha and freq
    f = getFreq(myStr)
    rf = relativeFreq(f,strLen)
    #Testing
    #for i in range(0,26):
    #    print(alpha[i], f[i], rf[i])
    #plot alpha vs relFreq
    #PLOTTING
    plot.title("Relative Frequency graph")
    plot.xlabel("Letter")
    plot.ylabel("Relative frequency(%)")
    for i in range(0,26):
        plot.annotate(rf[i],xy=(alpha[i],rf[i]),ha='center',fontsize=5)
    #maybe try except
    try:
        plot.bar(alpha, rf)
        plot.show() #needs this to actually show the plot
    except:
        print("Some error: Can't show graph")


