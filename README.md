<h2>Cryptographic functions</h2>
Contains a python program that lets you select from 4 options: frequency plot, affine cipher, DES and RSA.
The 4 modules are implement the cryptographic function or encryption/decryption "from scratch" to demonstrate
their inner workings


<h3>Dependencies</h3>
Should have the following installed:
    Python 3.10.12
    matplotlib 3.9.1 (only for frequency plot)
    tornado 6.4.1 (only for frequency plot)


<h3>HOW TO USE</h3>
In terminal:
    python3 program.py
Then:
    select from options
    They will require a filename as input
    The encryption functions will create an output file, that the decrypt function will decrypt 

<b>1.Frequency Plot</b>
    Input filename: test1.txt
<b>2.Affine cipher</b>
    Input filename: test2.txt
<b>3.DES</b>
    Encrypt:
        Input filename: test3.txt
        Input key:hello
        >outputs: desOutput.txt
    Decrypt:
        Input:none
        Output:none
<b>4.RSA</b>
    Encrypt:
        Input: test4.txt
        >outputs: public_key.txt, private_key.txt, cipher.txt
    Decrypt:
        Input:none
        Output:none
