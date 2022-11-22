

name = input("Name: ")
print("Welcome" , name)
start = input("Would you like to play? y/n " )
for i in start:
    if start == "y":
        pass
    else:
        break

import random 
from random import randint
num = random.randint(1,10)
guess = None
tries = 0
while guess != num:
    guess = input("You have 3 tries! Pease enter any number from 1 to 10: ")
    guess = int(guess)
    tries = tries + 1
    if tries == 3:
        print("You've failed! No more tries! See you next time!")
        break
    if guess == num:
        print("Congratulations! Good job!")
        break
    else:
        print("Wrong number! Please try again!")
       
        