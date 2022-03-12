import random
from enum import Enum

charactersGuessed = []

def choose_line(file_name): 
	with open(file_name, 'r', encoding='utf16') as file: # you need UTF16 when file was written by Powershell
		lines = file.readlines() 
		random_line = random.choice(lines)
	return random_line 

class AnswerState(Enum):
	NoMatch = 0
	Match = 1
	DuplicateMatch = 2
	InvalidCharacter = 3
	InvalidLength = 4
	NoInput = 5
	DuplicateNoMatch = 6

def EvaluateAnswerState(answer, hint, guess):
	# no input
	if not guess:
		return AnswerState.NoInput
	# too long
	if len(guess) > 1:
		# we're going to allow for a cheat:
		# you can type in the entire answer,
		# allowing for immediate exit.
		if guess == answer:
			return AnswerState.Match
		return AnswerState.InvalidLength
	# invalid input
	if not guess.isalpha():
		return AnswerState.InvalidCharacter	
	# DuplicateMatch
	if guess in hint:
		return AnswerState.DuplicateMatch
	# Match
	if guess in answer:
		return AnswerState.Match
	# DuplicateGuess
	if charactersGuessed.count(guess) > 0:
		return AnswerState.DuplicateNoMatch
	# store already guessed characters
	if not charactersGuessed.count(guess) > 0:
		charactersGuessed.append(guess)
	# implement and include flag here for both Duplicate and NoMatch? 
	# NoMatch (default)
	return AnswerState.NoMatch

def ReplaceCharacterInHint(answer, hint, char):
	newHint = [None] * len(answer) # declare empty list of size answer
	# loop over hint to get what we already got, including hint indicator
	for i, j in enumerate(hint):
		newHint[i] = j
	# get matching char from answer and put it in hint
	for x, y in enumerate(answer):
		if y == char:
			newHint[x] = y
	return ''.join(newHint) # return list as string