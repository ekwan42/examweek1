import random

x=random.randint(1,100)

a=1
e=0
print("Welcome to the Number Guessing Game!""\n"
      "Try to guess the number between 1 and 100""\n")
while a==1:
    print("Enter your guess : ")
    e=e+1
    b=int(input())
    if b<1 or b>100:
        print("Guess the number between 1 and 100")
    elif b>x:
        print("Too high")
    elif b<x:
        print("Too low")
    else:
        print("Congratulations! You've guessed the number in ",e,"attempts")
        break