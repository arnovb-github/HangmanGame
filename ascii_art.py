# holds the ascii art to be displayed
# we will assume a maximum of 10 turns

# I think we should use a tuple over a list

# one of the challenges is how we combine the
# upright post from the second guess with the man hanging?
# we could define the entire 'picture' for all guesses,
# but that gets tedious.

HANGMAN_PICS = ['''




     ''','''




     ===''','''
      +
      |
      |
      |
     ===''','''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']