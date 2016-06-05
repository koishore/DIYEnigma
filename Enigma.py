# Roy, Koishore
# Trends in History
# Professor Gwen Kelly
# 01/05/2016
# Enigma.py

import os

choice = 0

while ((choice < 1) or (choice > 2)):
    
    choice = int(raw_input('\nEnter \n\t<1> to encrypt a message \n\t<2> to decrypt a message:'))

def encrypt (str):

    num1 = 0
    num2 = 0
    num3 = 0
    
    while ((num1 < 1) or (num1 > 8)):
    
        num1 = int(raw_input('\nEnter the first rotor number (Only numbers between 1 and 8 are acceptable):'))

    while ((num2 < 1) or (num2 > 8)):
    
        num2 = int(raw_input('\nEnter the second rotor number (Only numbers between 1 and 8 are acceptable):'))

    while ((num3 < 1) or (num3 > 8)):
    
        num3 = int(raw_input('\nEnter the third rotor number (Only numbers between 1 and 8 are acceptable):'))

    rotor1 = {'a':'e', 'b':'k', 'c':'m', 'd':'f', 'e':'l', 'f':'g', 'g':'d', 'h':'q', 'i':'v', 'j':'z', 'k':'n', 'l':'t', 'm':'o', 'n':'w', 'o':'y', 'p':'h', 'q':'x', 'r':'u', 's':'s', 't':'p', 'u':'a', 'v':'i', 'w':'b', 'x':'r', 'y':'c', 'z':'j', 'A':'E', 'B':'K', 'C':'M', 'D':'F', 'E':'L', 'F':'G', 'G':'D', 'H':'Q', 'I':'V', 'J':'Z', 'K':'N', 'L':'T', 'M':'O', 'N':'W', 'O':'Y', 'P':'H', 'Q':'X', 'R':'U', 'S':'S', 'T':'P', 'U':'A', 'V':'I', 'W':'B', 'X':'R', 'Y':'C', 'Z':'J'}
    rotor2 = {'a':'a', 'b':'j', 'c':'d', 'd':'k', 'e':'s', 'f':'i', 'g':'r', 'h':'u', 'i':'x', 'j':'b', 'k':'l', 'l':'h', 'm':'w', 'n':'t', 'o':'m', 'p':'c', 'q':'q', 'r':'g', 's':'z', 't':'n', 'u':'p', 'v':'y', 'w':'f', 'x':'v', 'y':'o', 'z':'e', 'A':'A', 'B':'J', 'C':'D', 'D':'K', 'E':'S', 'F':'I', 'G':'R', 'H':'U', 'I':'X', 'J':'B', 'K':'L', 'L':'H', 'M':'W', 'N':'T', 'O':'M', 'P':'C', 'Q':'Q', 'R':'G', 'S':'Z', 'T':'N', 'U':'P', 'V':'Y', 'W':'F', 'X':'V', 'Y':'O', 'Z':'E'}
    rotor3 = {'a':'b', 'b':'d', 'c':'f', 'd':'h', 'e':'j', 'f':'l', 'g':'c', 'h':'p', 'i':'r', 'j':'t', 'k':'x', 'l':'v', 'm':'z', 'n':'n', 'o':'y', 'p':'e', 'q':'i', 'r':'w', 's':'g', 't':'a', 'u':'k', 'v':'m', 'w':'u', 'x':'s', 'y':'q', 'z':'o', 'A':'B', 'B':'D', 'C':'F', 'D':'H', 'E':'J', 'F':'L', 'G':'C', 'H':'P', 'I':'R', 'J':'T', 'K':'X', 'L':'V', 'M':'Z', 'N':'N', 'O':'Y', 'P':'E', 'Q':'I', 'R':'W', 'S':'G', 'T':'A', 'U':'K', 'V':'M', 'W':'U', 'X':'S', 'Y':'Q', 'Z':'O'}
    rotor4 = {'a':'e', 'b':'s', 'c':'o', 'd':'v', 'e':'p', 'f':'z', 'g':'j', 'h':'a', 'i':'y', 'j':'q', 'k':'u', 'l':'i', 'm':'r', 'n':'h', 'o':'x', 'p':'l', 'q':'n', 'r':'f', 's':'t', 't':'g', 'u':'k', 'v':'d', 'w':'c', 'x':'m', 'y':'w', 'z':'b', 'A':'E', 'B':'S', 'C':'O', 'D':'V', 'E':'P', 'F':'Z', 'G':'J', 'H':'A', 'I':'Y', 'J':'Q', 'K':'U', 'L':'I', 'M':'R', 'N':'H', 'O':'X', 'P':'L', 'Q':'N', 'R':'F', 'S':'T', 'T':'G', 'U':'K', 'V':'D', 'W':'C', 'X':'M', 'Y':'W', 'Z':'B'}
    rotor5 = {'a':'v', 'b':'z', 'c':'b', 'd':'r', 'e':'g', 'f':'i', 'g':'t', 'h':'y', 'i':'u', 'j':'p', 'k':'s', 'l':'d', 'm':'n', 'n':'h', 'o':'l', 'p':'x', 'q':'a', 'r':'w', 's':'m', 't':'j', 'u':'q', 'v':'o', 'w':'f', 'x':'e', 'y':'c', 'z':'k', 'A':'V', 'B':'Z', 'C':'B', 'D':'R', 'E':'G', 'F':'I', 'G':'T', 'H':'Y', 'I':'U', 'J':'P', 'K':'S', 'L':'D', 'M':'N', 'N':'H', 'O':'L', 'P':'X', 'Q':'A', 'R':'W', 'S':'M', 'T':'J', 'U':'Q', 'V':'O', 'W':'F', 'X':'E', 'Y':'C', 'Z':'K'}
    rotor6 = {'a':'j', 'b':'p', 'c':'g', 'd':'v', 'e':'o', 'f':'u', 'g':'m', 'h':'f', 'i':'y', 'j':'q', 'k':'b', 'l':'e', 'm':'n', 'n':'h', 'o':'z', 'p':'r', 'q':'d', 'r':'k', 's':'a', 't':'s', 'u':'x', 'v':'l', 'w':'i', 'x':'c', 'y':'t', 'z':'w', 'A':'J', 'B':'P', 'C':'G', 'D':'V', 'E':'O', 'F':'U', 'G':'M', 'H':'F', 'I':'Y', 'J':'Q', 'K':'B', 'L':'E', 'M':'N', 'N':'H', 'O':'Z', 'P':'R', 'Q':'D', 'R':'K', 'S':'A', 'T':'S', 'U':'X', 'V':'L', 'W':'I', 'X':'C', 'Y':'T', 'Z':'W'}
    rotor7 = {'a':'n', 'b':'z', 'c':'j', 'd':'h', 'e':'g', 'f':'r', 'g':'c', 'h':'x', 'i':'m', 'j':'y', 'k':'s', 'l':'w', 'm':'b', 'n':'o', 'o':'u', 'p':'f', 'q':'a', 'r':'i', 's':'v', 't':'l', 'u':'p', 'v':'e', 'w':'k', 'x':'q', 'y':'d', 'z':'t', 'A':'N', 'B':'Z', 'C':'J', 'D':'H', 'E':'G', 'F':'R', 'G':'C', 'H':'X', 'I':'M', 'J':'Y', 'K':'S', 'L':'W', 'M':'B', 'N':'O', 'O':'U', 'P':'F', 'Q':'A', 'R':'I', 'S':'V', 'T':'L', 'U':'P', 'V':'E', 'W':'K', 'X':'Q', 'Y':'D', 'Z':'T'}
    rotor8 = {'a':'f', 'b':'k', 'c':'q', 'd':'h', 'e':'t', 'f':'l', 'g':'x', 'h':'o', 'i':'c', 'j':'b', 'k':'j', 'l':'s', 'm':'p', 'n':'d', 'o':'z', 'p':'r', 'q':'a', 'r':'m', 's':'e', 't':'w', 'u':'n', 'v':'i', 'w':'u', 'x':'y', 'y':'g', 'z':'v', 'A':'F', 'B':'K', 'C':'Q', 'D':'H', 'E':'T', 'F':'L', 'G':'X', 'H':'O', 'I':'C', 'J':'B', 'K':'J', 'L':'S', 'M':'P', 'N':'D', 'O':'Z', 'P':'R', 'Q':'A', 'R':'M', 'S':'E', 'T':'W', 'U':'N', 'V':'I', 'W':'U', 'X':'Y', 'Y':'G', 'Z':'V'}
        
    textletter1 = ''
    textletter2 = ''
    textletter3 = ''
	
    for line1 in str:

        for letter1 in line1:

            if letter1.isalpha():

                if num1 == 1:

                    letter1 = rotor1[letter1]

                elif num1 == 2:
                            
                    letter1 = rotor2[letter1]
                    
                elif num1 == 3:
                                    
                    letter1 = rotor3[letter1]
                    
                elif num1 == 4:
                                            
                    letter1 = rotor4[letter1]

                elif num1 == 5:
                                                    
                    letter1 = rotor5[letter1]
                    
                elif num1 == 6:
                                                            
                    letter1 = rotor6[letter1]

                elif num1 == 7:
                                                                    
                    letter1 = rotor7[letter1]

                elif num1 == 8:
                                                                            
                    letter1 = rotor8[letter1]

            textletter1 = textletter1 + letter1
                
    for line2 in textletter1:
                    
        for letter2 in line2:

            if letter2.isalpha():
    
                if num2 == 1:
        
                    letter2 = rotor1[letter2]
            
                elif num2 == 2:
                
                    letter2 = rotor2[letter2]
                
                elif num2 == 3:
                    
                    letter2 = rotor3[letter2]
                
                elif num2 == 4:
                    
                    letter2 = rotor4[letter2]
                
                elif num2 == 5:
                    
                    letter2 = rotor5[letter2]
                
                elif num2 == 6:
                    
                    letter2 = rotor6[letter2]
                
                elif num2 == 7:
                    
                    letter2 = rotor7[letter2]
                
                elif num2 == 8:
                    
                    letter2 = rotor8[letter2]
    
            textletter2 = textletter2 + letter2

    for line3 in textletter2:
    
        for letter3 in line3:
        
            if letter3.isalpha():
            
                if num3 == 1:
                
                    letter3 = rotor1[letter3]
                
                elif num3 == 2:
                    
                    letter3 = rotor2[letter3]
                
                elif num3 == 3:
                    
                    letter3 = rotor3[letter3]
        
                elif num3 == 4:
                
                    letter3 = rotor4[letter3]
                
                elif num3 == 5:
                    
                    letter3 = rotor5[letter3]
    
                elif num3 == 6:
                
                    letter3 = rotor6[letter3]
                
                elif num3 == 7:
                    
                    letter2 = rotor7[letter3]
            
                elif num3 == 8:
                
                    letter3 = rotor8[letter3]
                    
            textletter3 = textletter3 + letter3

    return textletter3

def decrypt (str):
    
    num1 = 0
    num2 = 0
    num3 = 0
    
    while ((num1 < 1) or (num1 > 8)):
        
        num1 = int(raw_input('\nEnter the first rotor number (Only numbers between 1 and 8 are acceptable):'))

    while ((num2 < 1) or (num2 > 8)):
        
        num2 = int(raw_input('\nEnter the second rotor number (Only numbers between 1 and 8 are acceptable):'))

    while ((num3 < 1) or (num3 > 8)):
    
        num3 = int(raw_input('\nEnter the third rotor number (Only numbers between 1 and 8 are acceptable):'))
    
    rotor1 = {'J':'Z', 'C':'Y', 'R':'X', 'B':'W', 'I':'V', 'A':'U', 'P':'T', 'S':'S', 'U':'R', 'X':'Q', 'H':'P', 'Y':'O', 'W':'N', 'O':'M', 'T':'L', 'N':'K', 'Z':'J', 'V':'I', 'Q':'H', 'D':'G', 'G':'F', 'L':'E', 'F':'D', 'M':'C', 'K':'B', 'E':'A', 'j':'z', 'c':'y', 'r':'x', 'b':'w', 'i':'v', 'a':'u', 'p':'t', 's':'s', 'u':'r', 'x':'q', 'h':'p', 'y':'o', 'w':'n', 'o':'m', 't':'l', 'n':'k', 'z':'j', 'v':'i', 'q':'h', 'd':'g', 'g':'f', 'l':'e', 'f':'d', 'm':'c', 'k':'b', 'e':'a'}
    rotor2 = {'E':'Z', 'O':'Y', 'V':'X', 'F':'W', 'Y':'V', 'P':'U', 'N':'T', 'Z':'S', 'G':'R', 'Q':'Q', 'C':'P', 'M':'O', 'T':'N', 'W':'M', 'H':'L', 'L':'K', 'B':'J', 'X':'I', 'U':'H', 'R':'G', 'I':'F', 'S':'E', 'K':'D', 'D':'C', 'J':'B', 'A':'A', 'e':'z', 'o':'y', 'v':'x', 'f':'w', 'y':'v', 'p':'u', 'n':'t', 'z':'s', 'g':'r', 'q':'q', 'c':'p', 'm':'o', 't':'n', 'w':'m', 'h':'l', 'l':'k', 'b':'j', 'x':'i', 'u':'h', 'r':'g', 'i':'f', 's':'e', 'k':'d', 'd':'c', 'j':'b', 'a':'a'}
    rotor3 = {'O':'Z', 'Q':'Y', 'S':'X', 'U':'W', 'M':'V', 'K':'U', 'A':'T', 'G':'S', 'W':'R', 'I':'Q', 'E':'P', 'Y':'O', 'N':'N', 'Z':'M', 'V':'L', 'X':'K', 'T':'J', 'R':'I', 'P':'H', 'C':'G', 'L':'F', 'J':'E', 'H':'D', 'F':'C', 'D':'B', 'B':'A', 'o':'z', 'q':'y', 's':'x', 'u':'w', 'm':'v', 'k':'u', 'a':'t', 'g':'s', 'w':'r', 'i':'q', 'e':'p', 'y':'o', 'n':'n', 'z':'m', 'v':'l', 'x':'k', 't':'j', 'r':'i', 'p':'h', 'c':'g', 'l':'f', 'j':'e', 'h':'d', 'f':'c', 'd':'b', 'b':'a'}
    rotor4 = {'B':'Z', 'W':'Y', 'M':'X', 'C':'W', 'D':'V', 'K':'U', 'G':'T', 'T':'S', 'F':'R', 'N':'Q', 'L':'P', 'X':'O', 'H':'N', 'R':'M', 'I':'L', 'U':'K', 'Q':'J', 'Y':'I', 'A':'H', 'J':'G', 'Z':'F', 'P':'E', 'V':'D', 'O':'C', 'S':'B', 'E':'A', 'b':'z', 'w':'y', 'm':'x', 'c':'w', 'd':'v', 'k':'u', 'g':'t', 't':'s', 'f':'r', 'n':'q', 'l':'p', 'x':'o', 'h':'n', 'r':'m', 'i':'l', 'u':'k', 'q':'j', 'y':'i', 'a':'h', 'j':'g', 'z':'f', 'p':'e', 'v':'d', 'o':'c', 's':'b', 'e':'a'}
    rotor5 = {'K':'Z', 'C':'Y', 'E':'X', 'F':'W', 'O':'V', 'Q':'U', 'J':'T', 'M':'S', 'W':'R', 'A':'Q', 'X':'P', 'L':'O', 'H':'N', 'N':'M', 'D':'L', 'S':'K', 'P':'J', 'U':'I', 'Y':'H', 'T':'G', 'I':'F', 'G':'E', 'R':'D', 'B':'C', 'Z':'B', 'V':'A', 'k':'z', 'c':'y', 'e':'x', 'f':'w', 'o':'v', 'q':'u', 'j':'t', 'm':'s', 'w':'r', 'a':'q', 'x':'p', 'l':'o', 'h':'n', 'n':'m', 'd':'l', 's':'k', 'p':'j', 'u':'i', 'y':'h', 't':'g', 'i':'f', 'g':'e', 'r':'d', 'b':'c', 'z':'b', 'v':'a'}
    rotor6 = {'W':'Z', 'T':'Y', 'C':'X', 'I':'W', 'L':'V', 'X':'U', 'S':'T', 'A':'S', 'K':'R', 'D':'Q', 'R':'P', 'Z':'O', 'H':'N', 'N':'M', 'E':'L', 'B':'K', 'Q':'J', 'Y':'I', 'F':'H', 'M':'G', 'U':'F', 'O':'E', 'V':'D', 'G':'C', 'P':'B', 'J':'A', 'w':'z', 't':'y', 'c':'x', 'i':'w', 'l':'v', 'x':'u', 's':'t', 'a':'s', 'k':'r', 'd':'q', 'r':'p', 'z':'o', 'h':'n', 'n':'m', 'e':'l', 'b':'k', 'q':'j', 'y':'i', 'f':'h', 'm':'g', 'u':'f', 'o':'e', 'v':'d', 'g':'c', 'p':'b', 'j':'a'}
    rotor7 = {'T':'Z', 'D':'Y', 'Q':'X', 'K':'W', 'E':'V', 'P':'U', 'L':'T', 'V':'S', 'I':'R', 'A':'Q', 'F':'P', 'U':'O', 'O':'N', 'B':'M', 'W':'L', 'S':'K', 'Y':'J', 'M':'I', 'X':'H', 'C':'G', 'R':'F', 'G':'E', 'H':'D', 'J':'C', 'Z':'B', 'N':'A', 't':'z', 'd':'y', 'q':'x', 'k':'w', 'e':'v', 'p':'u', 'l':'t', 'v':'s', 'i':'r', 'a':'q', 'f':'p', 'u':'o', 'o':'n', 'b':'m', 'w':'l', 's':'k', 'y':'j', 'm':'i', 'x':'h', 'c':'g', 'r':'f', 'g':'e', 'h':'d', 'j':'c', 'z':'b', 'n':'a'}
    rotor8 = {'V':'Z', 'G':'Y', 'Y':'X', 'U':'W', 'I':'V', 'N':'U', 'W':'T', 'E':'S', 'M':'R', 'A':'Q', 'R':'P', 'Z':'O', 'D':'N', 'P':'M', 'S':'L', 'J':'K', 'B':'J', 'C':'I', 'O':'H', 'X':'G', 'L':'F', 'T':'E', 'H':'D', 'Q':'C', 'K':'B', 'F':'A', 'v':'z', 'g':'y', 'y':'x', 'u':'w', 'i':'v', 'n':'u', 'w':'t', 'e':'s', 'm':'r', 'a':'q', 'r':'p', 'z':'o', 'd':'n', 'p':'m', 's':'l', 'j':'k', 'b':'j', 'c':'i', 'o':'h', 'x':'g', 'l':'f', 't':'e', 'h':'d', 'q':'c', 'k':'b', 'f':'a'}
    
    textletter1 = ''
    textletter2 = ''
    textletter3 = ''
    
    for line1 in str:
        
        for letter1 in line1:
            
            if letter1.isalpha():
                
                if num3 == 1:
                    
                    letter1 = rotor1[letter1]
                
                elif num3 == 2:
                    
                    letter1 = rotor2[letter1]
                
                elif num3 == 3:
                    
                    letter1 = rotor3[letter1]
                
                elif num3 == 4:
                    
                    letter1 = rotor4[letter1]
                
                elif num3 == 5:
                    
                    letter1 = rotor5[letter1]
                
                elif num3 == 6:
                    
                    letter1 = rotor6[letter1]
                
                elif num3 == 7:
                    
                    letter1 = rotor7[letter1]
                
                elif num3 == 8:
                    
                    letter1 = rotor8[letter1]
    
            textletter1 = textletter1 + letter1

    for line2 in textletter1:
    
        for letter2 in line2:
        
            if letter2.isalpha():
            
                if num2 == 1:
                
                    letter2 = rotor1[letter2]
                
                elif num2 == 2:
                    
                    letter2 = rotor2[letter2]
                
                elif num2 == 3:
                    
                    letter2 = rotor3[letter2]
        
                elif num2 == 4:
                
                    letter2 = rotor4[letter2]
                
                elif num2 == 5:
                    
                    letter2 = rotor5[letter2]
    
                elif num2 == 6:
                
                    letter2 = rotor6[letter2]
                
                elif num2 == 7:
                    
                    letter2 = rotor7[letter2]
            
                elif num2 == 8:
                
                    letter2 = rotor8[letter2]
                    
            textletter2 = textletter2 + letter2

    for line3 in textletter2:
    
        for letter3 in line3:
        
            if letter3.isalpha():
            
                if num1 == 1:
                
                    letter3 = rotor1[letter3]
                
                elif num1 == 2:
                    
                    letter3 = rotor2[letter3]
        
                elif num1 == 3:
                
                    letter3 = rotor3[letter3]
                
                elif num1 == 4:
                    
                    letter3 = rotor4[letter3]
                
                elif num1 == 5:
                    
                    letter3 = rotor5[letter3]
    
                elif num1 == 6:
                
                    letter3 = rotor6[letter3]
                
                elif num1 == 7:
                    
                    letter2 = rotor7[letter3]
            
                elif num1 == 8:
                
                    letter3 = rotor8[letter3]
                    
            textletter3 = textletter3 + letter3

    return textletter3

if os.path.exists("message.txt"):
    
    text = open ("message.txt","r")

    if choice == 1:

        output = encrypt (text)
        print '\nYour message has been encrypted using the rotor key and is saved in a file named message.txt!"'
    
    elif choice == 2:

        output = decrypt (text)
        print '\nYour message has been decrypted using the rotor key and is saved in a file named message.txt!"'
    
    target = open ("message.txt","w")
    target.write (output)
    target.close ()


else:
    
    print '\nSorry. No file named message.txt exists!'