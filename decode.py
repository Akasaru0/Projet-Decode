#!/usr/bin/env python
import sys


def help():
    #To default, It's the English Help page
    if len(sys.argv)== 2:
        f = open('help_en.txt', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
    else:
        #This is for the Frensh Help page
        if sys.argv[2] == "fr":
            f = open('help_fr.txt', 'r')
            file_contents = f.read()
            print (file_contents)
            f.close()
        #This is for the English Help page
        if sys.argv[2] == "en":
            f = open('help_en.txt', 'r')
            file_contents = f.read()
            print (file_contents)
            f.close()
        


def decode_hexa():
    a = arg_hexa
    print(bytes.fromhex(a).decode('utf-8'))

nb_of_arg = len(sys.argv)-1
agr_hexa = 0

if len(sys.argv)== 1:
    #This is the test if there is no agrument
    print("Warning! there is no argument.")
    print("Please type ./decode help to see the help manual.")
else:
    #There is the test for the arg help
    if sys.argv[1] == "help":
        help()
    else:
        text = sys.argv[1]
        if text.startswith(":") == False:
            print("/!\ Error (001):The Hash is not specified!")
        else:
            Hash = text[1:]
            print(Hash)
            if sys.argv[i] == "-dh":
                print(len(sys.argv))
