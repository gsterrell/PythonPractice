# This is a sample Python script.

# Press Shift+F10 to execute it or replace it wit1h your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import guessing_game

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    selection = int(input("Enter your program selection: \n1) Guessing Game.\n"))

    if selection == 1:
        guessing_game.guessing_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
