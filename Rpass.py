# rnadom password generator.

import random

char = 'abcdefghijklmnopqrstuv1234567890ABCDEFGHIJKLMNOPQRSTUV!@#$%^&*'
number = input('Number of PWs: ')
number = int(number)

length = input('Password length: ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length): 
        password += random.choice(char)
    print(password)
