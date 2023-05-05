import string
import random
validchars='abcdefghijklmnopqrstuvwxyz1234567890'
loginlen=random.randint(4,15)
login=''
length = 15
 
print('''Choose character set for password from these :
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
characterList = ""
 
while(True):
    choice = int(input("Pick a number for which type of password you want (You can chose all character)-:"))
    if(choice == 1):
         
        characterList += string.ascii_letters
    elif(choice == 2):
         
        characterList += string.digits
    elif(choice == 3):
         
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    randomchar = random.choice(characterList)
    password.append(randomchar)
 
# printing password as a string
for i in range(loginlen):
    pos=random.randint(0,len(validchars)-1)
    login=login+validchars[pos]
if login[0].isnumeric():
    pos=random.randint(0,len(validchars)-10)
    login=validchars[pos]+login
servers=['@gmail']
servpos=random.randint(0,len(servers)-1)
email=login+servers[servpos]
tlds=['.com']
tldpos=random.randint(0,len(tlds)-1)
email=email+tlds[tldpos]
print(email+"\n")
print("Your Email's password is " + "".join(password))