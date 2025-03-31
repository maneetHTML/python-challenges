import random
import string
le=int(input('enter your number of letters :'))
char=string.ascii_letters
char +=string.digits
password ='' 
for i in range(le):
    next_character = random.choice(char)
    password += next_character
print("Your Random password is : ",password )