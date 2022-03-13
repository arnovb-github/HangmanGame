# An implementation of Hangman
# I prefer this version over hangman2.py, 
# because the 'UI' and logic are separated.
# By 'UI' I mean any code that does print().
# Nowhere should we use print() except in this file and
# also this file should not contain any 'business logic',
# even it is just hangman.
# The problem with this version is that it is hard to remain DRY,
# because some of the states that the 'backend' returns 
# (i.e. what comes from the utils.py stuff)
# are difficult to incorporate in the logic flow.
# Specifically, there is some code duplication after DuplicateNoMatch and NoMatch.
# It is just 3 lines, but it is still really ugly 
# and I am struggling to find a good way to get rid of it.
# I suppose we ideally should refactor this to a point where main() just calls play(),
# where play() does the 'UI' stuff,
# but that doesn't make the DRY problem go a away.

import sys
import argparse
from utils import *
from ascii_art import *

numGuesses = 10
hintIndicator = "_"
description = f"""
Hangman game
--------------
Can you guess the word in {numGuesses} tries?
"""

def main(argv):
    # get command line arguments
    args = cli(argv)
    easyMode = args.easy
    # preliminary setup
    # we should allow for a custom wordlist to be passed in,
    # but for now we define one in the same path as the script
    wordList = ".\woordenlijst.txt" # generated by PowerShell from larger OpenTaal source file
    answer = choose_line(wordList)
    wordLength = len(answer)
    hint = hintIndicator * wordLength
    guessesLeft = numGuesses # guessesLeft will decrement
    # main program loop
    while guessesLeft > 0:

        print('H A N G M A N')
        print(HANGMAN_PICS[numGuesses - guessesLeft])
        print(hint)
        print("")
        guess = input(f"Please enter a single character to guess:\nYou have {guessesLeft} tries left.\n" )
        state = EvaluateAnswerState(answer, hint, guess)
        match state:
            case AnswerState.NoInput:
                print("No input provided. Please try again")
                continue
            case AnswerState.InvalidCharacter:
                print("Invalid character input. Please try again.")
                continue
            case AnswerState.InvalidLength:
                print("Invalid input length. Please try again.")
                continue
            case AnswerState.DuplicateMatch:
                print(f"You already found the character '{guess}'. Please try again.")
                continue
            case AnswerState.DuplicateNoMatch:
                if easyMode:
                    print(f"You already tried '{guess}' silly!")
                    continue
                else:
                    print(f"Too bad. The answer does not contain '{guess}'.")
                    # code challenge
                    # duplicate of NoMatch output. Ideally want to refactor (DRY principle) but not sure how yet.
                    # the simplest way would probably to move the logic from EvaluateAnswerState to main loop,
                    # but that would make the logic more messy, being intertwined with the 'UI' part.
                    guessesLeft -= 1
                    if guessesLeft > 0:
                        continue
            case AnswerState.NoMatch:
                print(f"Too bad. The answer does not contain '{guess}'.")
                guessesLeft -= 1
                if guessesLeft > 0:
                    continue
            case AnswerState.Match:
                hint = ReplaceCharacterInSameSizedString(answer, hint, guess)
                if hint == answer or guess == answer:
                    print(f"Congratulations! You found the answer '{answer}' with {guessesLeft} tries left.")
                    input("Press Enter to close the program.")
                    break
                print(f"Nice one! The answer does indeed contain '{guess}'.")
                continue
        print(f"Oh dear. You did not guess the word. The word was '{answer}'. Better luck next time.")

class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
    pass # do nothing

def cli(argv):
    parser = argparse.ArgumentParser(
        prog=argv[0],
        description=description,
        formatter_class=CustomFormatter)

    parser.add_argument(
        "--easy", "-e",
        action='store_true',
        help="Remembers what characters you already tried.")

    args = parser.parse_args(argv[1:])

    return args

if __name__ == '__main__':
    sys.exit(main(sys.argv))