# Game where we have to guess random numbers , and computer will tell in how tries we were able to guess it 
'''
import random
number = random.randint(1, 100)
guesses = 0
guess = int(input("Guess a number btw 1 and 100: ") )
guesses += 1

while guess != number:
    if guess < number:
        print("Too low!!")
    else: 
        print("Too high!")

    guess = int(input("Guess again: "))
    guesses += 1


print("Great! You have accurately guessed the number!!")
print("You took", guesses, "tries.")


#######

import random

number = random.randint(1, 100)

guesses = 0 
max_guesses = 10

print("Choose a number between 1 and 100")
print("You have 10 guesses to find it ")

while guesses < max_guesses:

    guess = int(input("Enter your guess : "))
    guesses += 1

    if guess < number :
        print("Too low")

    elif guess > number:
        print("Too high")
    else : 
        print("Congratulations ! You guesses the number ")
        print("The number was:" , number)
        print("You took", guesses, "tries.")
        break

if guesses == max_guesses:
    print("Sorry! You have used all your guesses.")
    print("The number was:", number)


import random

number = random.randint(1 ,100)
guesses = 0 
max_guesses = 10

print("Choose a number between 1 and 100")
print("You have 10 guesses to find it ")

while guesses < max_guesses:
    try:
        guess = int(input("Enter your guess : "))
    except ValueError:
        print("Please enter a valid input.")
        continue

    guesses += 1

    if guess < number :
        print("Too low")


    elif guess > number:
        print("Too high")    

    else :
        print("Congratulations ! You guessed the number ")
        print("The number was:" , number)
        print("You took", guesses, "tries.")
        break
if guesses == max_guesses and guess != number:
    print("Sorry! You have used all your guesses.")
    print("The number was:", number)
'''

import random

number = random.randint(1, 100)

guesses = 0
max_guesses = 10

print("I have chosen a number between 1 and 100.")
print("You have 10 guesses to find it!")

while guesses < max_guesses:

    try:
        guess = int(input("Enter your guess: "))

    except ValueError:
        print("Please enter a valid integer!")
        continue

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100!")
        continue

    guesses += 1

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("Congratulations! You guessed the number!")
        print("The number was:", number)
        print("It took you", guesses, "guesses.")
        break

if guesses == max_guesses and guess != number:
    print("Game over!")
    print("The number was:", number)

    




