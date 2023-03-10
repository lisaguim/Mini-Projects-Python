#Hangman game version 1 by lisa

import random
from os import system, name

# function to clear the screen in each execution
def clean_screen():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# game's function
def game():
    clean_screen()
    print("\nWelcome to the hangman game!")
    print("Guess the world below:\n")

    # word's list for the game
    words = ['banana', 'apple', 'orange', 'grape', 'watermelon']

    # randomly pick a word
    word = random.choice(words)

    # list comprehension
    letter_uncovered = ['_' for letter in word]

    # number of tentative
    #note: my hangman have 6 parts \o/
    chances = 6

    # list for the wrong letters
    wrong_letters = []

    #loop when the number of chances is highest than zero
    while chances > 0:
        print(" ".join(letter_uncovered))
        print('\nRemaining chances: ', chances)
        print("\nWrong letters: ", " ".join(wrong_letters))

        #tentative
        tentative = input("\nWrite a letter: ").lower()

        #conditional 1
        if tentative in word:
            index = 0
            for letter in word:
                if tentative == letter:
                     letter_uncovered[index] = letter
                index += 1
        else:
            chances -= 1
            wrong_letters.append(tentative)
        #conditional 2
        if "_" not in letter_uncovered:
            print("\nYou win! The word was: ", word)
    #conditional 3
    if "_" in letter_uncovered:
        print("\nYou lost! The word as: ", word)

#Main block
if __name__ == "__main__":
    game()
    print("\nThanks for play! :)\n")
