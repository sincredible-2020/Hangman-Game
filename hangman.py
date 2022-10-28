print("Welcome to Hangman game!")

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
''')

import hangmanwords
import random

words = hangmanwords.words
pics = hangmanwords.hangmanpics


def hangman():
    letter = ""
    wrong = 0
    guessed = 0
    guess = []
    already = ""

    aword = random.choice(words)
    for i in range(len(aword)):
        guess.append("_")

    while wrong != 7 and guessed != len(aword):
        letter = input("Guess a letter: ")
        if already == letter:
            print("You already guessed this letter.")
            letter = input("Guess a letter again: ")
        else:
            already = letter
            if letter in aword:
                for j in range(len(aword)):
                    if aword[j] == letter:
                        guess[j] = letter
                        guessed += 1
                print(''.join(guess))
            else:
                print(f"You guessed {letter}, that's not in the word. You lose a life.")
                print(pics[wrong])
                wrong += 1

    if guessed == len(aword):
        return "\nYou Win!"
    elif wrong == 7:
        return "\nYou Lose."

print(hangman())
