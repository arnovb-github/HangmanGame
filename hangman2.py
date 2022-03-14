# Another version, with the logic all in a single file
# This makes the code easier to follow
# and has the benefit of more fine-grained control over dataflow,
# but it does not have the clear separation of 'UI' and
# the backend logic that hangman.py has.
# This version is more DRY though.

import sys
from utils import *
from ascii_art import *
from cli_args import *

numGuesses = 10
hintIndicator = "_"

def main(argv):
    # get command line arguments
    args = cli(argv)
    easyMode = args.easy
    # preliminary setup
    # the wordList is a file that I generated using Powershell, 
    wordList = "woordenlijst.txt" # generated by PowerShell from larger OpenTaal source file
    answer = choose_line(wordList)
    wordLength = len(answer)
    hint = hintIndicator * wordLength
    guessesLeft = numGuesses # guessesLeft will decrement
    charactersGuessed = []
    # main program loop
    while guessesLeft > 0:

        print('H A N G M A N')
        print(HANGMAN_PICS[numGuesses - guessesLeft])
        print(hint)
        print("")
        guess = input(f"Please enter a single character to guess:\nYou have {guessesLeft} tries left.\n" )
        if not guess:
            print("No input provided. Please try again")
            continue

        if len(guess) > 1:
            print("Invalid character input. Please try again.")
            continue

        if not guess.isalpha():
            print("Invalid input length. Please try again.")
            continue

        if guess in hint:
            print(f"You already found the character '{guess}'. Please try again.")
            continue

        if charactersGuessed.count(guess) > 0 and guess not in answer:
            pass # fall through to NoMatch or DuplicateNoMatch.

        # DuplicateNoMatch
        if charactersGuessed.count(guess) > 0:
            if easyMode:
                print(f"You already tried '{guess}' silly!")
                continue

        # store already guessed characters
        if not charactersGuessed.count(guess) > 0:
            charactersGuessed.append(guess)

        if guess in answer:
            hint = ReplaceCharacterInSameSizedString(answer, hint, guess)
            if hint == answer or guess == answer:
                print(f"Congratulations! You found the answer '{answer}' with {guessesLeft} tries left.")
                input("Press Enter to close the program.")
                break
            print(f"Nice one! The answer does indeed contain '{guess}'.")
            continue

        # default is NoMatch
        print(f"Too bad. The answer does not contain '{guess}'.")
        guessesLeft -= 1
        if guessesLeft > 0:
            continue
        
        # No answer was found
        print(f"Oh dear. You did not guess the word. The word was '{answer}'. Better luck next time.")

if __name__ == '__main__':
    sys.exit(main(sys.argv))