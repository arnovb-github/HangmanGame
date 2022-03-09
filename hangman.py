from utils import *  # import all functionality from utils.py
from ascii_art import *

wordList = ".\woordenlijst.txt"
answer = choose_line(wordList).rstrip().lower() # if you don't strip you may be left with a dangling \r
hintIndicator = "_"
wordLength = len(answer)
hint = hintIndicator * wordLength
numGuesses = 10
guessesLeft = numGuesses

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
        case AnswerState.Duplicate:
            print(f"You already found the character {guess}. Please try again.")
            continue
        case AnswerState.NoMatch:
            print(f"Too bad. The answer does not contain '{guess}'.")
            guessesLeft -= 1
            if guessesLeft > 0:
                continue
        case AnswerState.Match:
            hint = ReplaceCharacterInHint(answer, hint, guess)
            if hint == answer:
                print(f"Congratulations! You found the answer '{answer}' in {numGuesses - guessesLeft} tries.")
                break
            print(f"Nice one! The answer does indeed contain '{guess}'.")
            continue
    print(f"Oh dear. You lost. The word was '{answer}'. Better luck next time.")