import random

random_num =random.randint(1,9)
guess = int(input("Guess a number between 1 and 9 : "))
if guess < random_num :
    print("Guessed too low")
elif guess > random_num:
    print ("Guessed too high")
else:
    print("guessed exactly the same")

