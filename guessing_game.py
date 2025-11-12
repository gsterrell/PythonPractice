from math import ceil
from math import log2
from math import log
import random


def guessing_game():
    print("Hi! Welcome to the Number Guessing Game.\nLet's start!")
    high = int(input("Enter an upper range: "))
    low = int(input("Enter an lower range: "))
    goal = random.randint(low, high) + 1
    chances = int(ceil(log(high - low + 1)) / log(2))
    try_count = 0;

    while try_count < chances:
        try_count += 1
        print(f'You have {chances - (try_count - 1)} chances to guess the answer.')
        guess = int(input("Your guess: "))
        if guess == goal:
            print("Correct guess!\nCongrats! You won")
            break
        elif try_count >= chances and guess != goal:
            print(f'Sorry! The number was {goal}. Better luck next time.')
        elif guess < goal:
            print("Too low. Guess again.")
        elif guess > goal:
            print("Too high. Guess again")
