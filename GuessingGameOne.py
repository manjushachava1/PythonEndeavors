# Program 9

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

rand = random.randint(1, 9)

print(rand)

guess = int(input("Guess a number between 1 and 9: "))

while guess != rand:
    guess = int(input("You're too low, guess again:")) if guess < rand else int(input("You're too high, guess again:"))

if guess == rand:
    print("You win!")
