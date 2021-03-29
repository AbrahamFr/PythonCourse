import random

roll = random.randint(1,6)

guess = int(input('Guess the roll:\n'))

if guess == roll:
    print("Correct! They rolled a " + str(roll))