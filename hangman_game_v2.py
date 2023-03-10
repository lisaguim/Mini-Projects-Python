#Hangman game version 2 by lisa

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

#function to drw the hangman
def display_hangman(chances):
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# game's function
def game():
    clean_screen()
    print("\nWelcometo hangman game!")
    print("Try to guess the world below:\n")

    # word's list for the game
    words = ['banana', 'apple', 'orange', 'grape', 'watermelon']

    # randomly pick a word
    word = random.choice(words)

    #list of letter of word
    word_list_letter = [letter for letter in word]

    board = ["_"] * len(word)

    # number of tentative
    chances = 6

    # list for letters used
    list_letters_used = []

    # loop when the number of chances is highest than zero
    while chances > 0:

        print(display_hangman(chances))
        print("The word is: ", board)
        print("\n")

        #tentative
        tentative = input("\nWrite a letter: ")

        #conditional 1
        if tentative in list_letters_used:
            print("You already used this letter. Try another one!")
            continue

        list_letters_used.append(tentative)

        #conditional2
        if tentative in word_list_letter:

            print("You're right!")

            #loop
            for indice in range(len(word_list_letter)):
                #conditional 1
                if word_list_letter[indice] == tentative:
                    board[indice] = tentative

            #if all the letter were inputed, so the game finished
            if "_" not in board:
                print("\nYou won ! The word was: ",format(word))
                break
        else:
            print("Ops. This letter is not in the word!")
            chances -=1

    #conditional1
    if "-" in board:
        print("\nYou lost! The word was: ",format(word))

#main block
if __name__ == "__main__":
    game()
    print("\nThanks for play!")