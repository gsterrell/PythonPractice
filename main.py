# This is a sample Python script.

# Press Shift+F10 to execute it or replace it wit1h your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from math import ceil
from math import log2
from math import log

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hi! Welcome to the Number Guessing Game.\nLet's start!")
    high = int(input("Enter an upper range: "))
    low = int(input("Enter an lower range: "))

    goal = random.randint(low, high)+1

    chances = int(ceil(log(high - low + 1)) / log(2))
    try_count = 0;

    print(f'You have {chances - (try_count - 1)} chances to guess the answer.\n')

    while try_count < chances:
        try_count += 1

        guess = int(input("Your guess: "))

        if guess == goal:
            print("Correct guess!\nCongrats! You won")
            break

        elif try_count >= chances and guess != goal:
            print(f'Sorry! The number was {goal}. Better luck next time.')

        elif guess < goal:
            int(input("Too low. Guess again: "))

        elif guess > goal:
            int(input("Too high. Guess again: "))

        print(f'\nYou have {chances - (try_count - 1)} chances to guess the answer.\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
