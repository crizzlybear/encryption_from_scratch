from frequency_plot import freq_plot
from affine_cipher import affine
from DES import des_encrypt, des_decrypt
from RSA import rsa_encrypt, rsa_decrypt, keySchedule
def main():
    exitMenu=0
    filename=""
    while(exitMenu==0):
        print("Select option")
        print("1.Frequency plot")
        print("2.Affine cipher")
        print("3.DES")
        print("4.RSA")
        print("0.Exit Program")
        menuSelection = input("Menu option:")
        if(menuSelection=="1"):
            print("!Frequency plot requires packages; matplotlib: pip install matplotlib and tornado ")
            filename = input("Enter filename: ")
            freq_plot(filename)
        elif(menuSelection=="2"):
            print("!Affine cipher")
            filename = input("Enter filename: ")
            affine(filename)
        elif(menuSelection=="3"):
            print("!DES")
            print("1.Encrypt file")
            print("2.Decrypt file")
            menuSelection2 = input("Menu option2: ")
            if(menuSelection2=="1"):
                print("encrypt")
                des_encrypt.DESencrypt()
            elif(menuSelection2=="2"):
                print("decrypt")
                des_decrypt.DESdecrypt()
            else:
                print("reselect")
        elif(menuSelection=="4"):
            print("!RSA")
            print("1.Encrypt file")
            print("2.Decrypt file")
            menuSelection2 = input("Menu option2: ")
            if(menuSelection2=="1"):
                print("encrypt")
                keySchedule.generateKeys()
                rsa_encrypt.RSAencrypt()
            elif(menuSelection2=="2"):
                print("decrypt")
                rsa_decrypt.RSAdecrypt()
            else:
                print("reselect")
        elif(menuSelection=="0"):
            print("Goodbye")
            exitMenu=1
        else:
            print("Select a valid option")

if __name__=='__main__':
    main()
