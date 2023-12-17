import random
import re
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits = ['1','2','3','4','5','6','7','8','9','0',]
specchara = ['@',',','!','"','£','$','%','^','&','*',')',')','-','_','+','=','[',']','{','}','<','>','.','/','?','~','#',':',';','¬','`']
passlength = int(input("How characters do you want your password to have?: "))
digitlength = int(input("How digits do you want your password to have?: "))
alphabetlength = int(input("How letters do you want your password to have?: "))
speccharalength = int(input("How special characters do you want your password to have?: "))
password = [ ]
while True:
 for x in range(1,passlength):
    characters1 = random.sample(alphabet, alphabetlength)
    characters2 = random.sample(digits, digitlength)
    characters3 = random.sample(specchara, speccharalength)
    characters = characters1 + characters2 + characters3
    random.shuffle(characters)
    password = "".join(characters)
 print(password)
 break