# This is a sample Python script.

# Press Shift+F10 to execute it or replace it wit1h your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import guessing_game
import word_guessing_game

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Available game options: ")
    print("1. Guessing Game")
    print("Number guessing game")
    print("Word Guessing Game")
    print("Hangman Game")
    print("21 Number Game")
    print("Rock Paper Scissor Game")
    # Check if two PDF documents are identical
    # Convert emoji into text
    # Create a Voice Recorder
    # Create a Screen recorder
    # Mastermind Game
    # 2048 Game
    # Flames game
    # Pokémon Training Game
    # Taking Screenshots using pyscreenshot
    # Desktop Notifier
    # Get Live Weather Desktop Notifications
    # How to use pynput to make a Keylogger?
    # Cows and Bulls game
    # Simple Attendance Tracker
    # Higher-Lower Game
    # Fun Fact Generator Web App
    # Creating payment receipts
    # How To Create a Countdown Timer?

    selection = int(input("Enter your program selection: \n1) Guessing Game.\n"))

    if selection == 1:
        guessing_game.guessing_game()
    elif selection == 2:
        word_guessing_game()
    else:
        print("Program not yet implemented")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
