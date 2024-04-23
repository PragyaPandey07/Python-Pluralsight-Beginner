import random

roll = random.randint(1,6)
guess = int(input("Guess the dice roll "))

if roll == guess :
    print("You guessed it right :), they rolled a " + str(roll))
else :
    print("You guessed wrong :(, they rolled a " + str(roll)) 