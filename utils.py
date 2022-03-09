import random
from enum import Enum

def choose_line(file_name): 
	with open(file_name, 'r', encoding='utf16') as file: # you need UTF16 when file was written by Powershell
		lines = file.readlines() 
		random_line = random.choice(lines)
	return random_line 

class AnswerState(Enum):
	NoMatch = 0
	Match = 1
	Duplicate = 2
	InvalidCharacter = 3
	InvalidLength = 4
	NoInput = 5

def EvaluateAnswerState(answer, hint, guess):
	# no input
	if not guess:
		return AnswerState.NoInput
	# too long
	if len(guess) > 1:
		return AnswerState.InvalidLength
	# invalid input
	if not guess.isalpha():
		return AnswerState.InvalidCharacter	
	# Duplicate
	if guess in hint:
		return AnswerState.Duplicate
	# Match
	if guess in answer:
		return AnswerState.Match
	# NoMatch (default)
	return AnswerState.NoMatch


def ReplaceCharacterInHint(answer, hint, char):
	newHint = [None] * len(answer) # declare list of size answer
	# loop over hint to get what we already got
	for i, j in enumerate(hint):
		newHint[i] = j
	# get matching char from answer and put it in hint
	for x, y in enumerate(answer):
		if y == char:
			newHint[x] = y
	return ''.join(newHint) # return list as string