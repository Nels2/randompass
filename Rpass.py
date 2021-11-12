# .Sypnosis: this is a random password generator. saves to a text file after the passwords are generated.
import random

char = 'abcdefghijklmnopqrstuv1234567890ABCDEFGHIJKLMNOPQRSTUV!@#$%^&*'
number = input('Number of passwords to create: ')
number = int(number)
length = input('Password length: ')
length = int(length)

f = open('createdPasswords.txt', "wb")
f.close()
for p in range(number):
    password = ''
    for c in range(length): 
        password += random.choice(char)
    x = password
    f = open('createdPasswords.txt', 'a')
    f.write(x + "\n")
    f.close()
    print(password)
print("you can view/copy the ("+ str(number) +") created passwords in createdPasswords.txt")
