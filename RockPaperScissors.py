# Program 8

# Make a two-player Rock-Paper-Scissors game.

import random

player = str(input("rock, paper, scissors: "))

choices = ("rock", "paper", "scissors")
word = random.choice(choices)

if player == "rock" and word == "paper":
    print("Computer chose " + word + " so you LOSE")

if player == "rock" and word == "scissors":
    print("Computer chose " + word + " so you WIN")

if player == "paper" and word == "rock":
    print("Computer chose " + word + " so you WIN")

if player == "paper" and word == "scissors":
    print("Computer chose " + word + " so you LOSE")

if player == "scissors" and word == "rock":
    print("Computer chose " + word + " so you LOSE")

if player == "scissors" and word == "paper":
    print("Computer chose " + word + " so you WIN")

if player == word:
    print("Its a Tie!")
