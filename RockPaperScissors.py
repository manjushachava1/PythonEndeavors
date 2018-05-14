# Make a two-player Rock-Paper-Scissors game.

import random

player = str(input("Rock, paper, scissors: "))

computer = random.sample(range(1, 4), 1)

# 1 = rock
# 2 = paper
# 3 = scissors
print(computer)

if player == "rock":
    if computer == 1:
        print("It's a Tie!")
elif player == "rock":
    if computer == 2 or 3:
        print("You either won or lost lel")