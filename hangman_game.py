import random
from collections import Counter


def hangman_game():
    some_words = '''apple banana mango strawberry 
    orange grape pineapple apricot lemon coconut watermelon 
    cherry papaya berry peach lychee muskmelon'''

    some_words = some_words.split()

    word = random.choice(some_words)

    print('Guess the word! Hint: word is a name of a fruit')
    print('You have {} guesses.'.format(len(word) + 2))

    for i in word:
        print('_', end=' ')
    print()

    # list for storing guessed letters
    letter_guessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            print('You have {} chances left.'.format(chances))
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # validating the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letter_guessed:
                print('You have already guess that letter')
                continue

            if guess in word:
                guess_occurs = word.count(guess)
                for _ in range(guess_occurs):
                    letter_guessed += guess

            # print the word
            for char in word:
                if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # if word is complete
                elif (Counter(letter_guessed) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print("Congratulations! You won!")
                    break   # to break out of the for loop
                else:
                    print('_', end=' ')

        # if user used all of their chances
        if chances <= 0 and (Counter(letter_guessed)) != Counter(word):
            print("\nYou lost. Try again...")
            print('The word was {}'.format(word))
            print()

    except KeyboardInterrupt:
        print('\nBye! Try again.\n')
        exit()






