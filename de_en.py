import re
import random

main_list =[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
              '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';',
                '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
                    'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f',
                      'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

def encryption():
    encrpt = ""
    spec = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd',
             'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm',
               ',', '.', '/', '`', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                 ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}',
                   '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C',
                     'V', 'B', 'N', 'M', '<', '>', '?']
    inp = input("enter your words: ")
    tpl = tuple(inp)
    lst = list(tpl)
    for i in lst:
        index = main_list.index(i)
        encrpt += random.choice(spec) + str(index) + random.choice(spec)
    print ("\n" + encrpt + "\n")
    
def decryption():
    dcrpt = ""
    encrpt_code = input("enter your encrypted code: ")
    encrpt_char = re.findall(r"\d+", encrpt_code)
    encrpt_list = list(encrpt_char)
    for i in incrpt_list:
        inti = int(i)
        dcrpt += main_list[inti]
    print ("\n" + dcrpt + "\n")

is_up = 1
while is_up == 1:
    choise = input("enter your choise ( encrypt=1 | decrypt=2 ) : ")
    if choise == "1":
        encryption()
    elif choise == "2":
        decryption()
    elif choise == "exit":
        is_up = 0
    else:
        print ("\nerr!! choise 1 or 2 ( encrypt=1 | decrypt=2 )\n")
