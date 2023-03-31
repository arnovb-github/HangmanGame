# holds the command line argument stuff

import argparse
import settings as gs

description = """
Hangman game
--------------
Can you guess the word in time?
"""

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

    parser.add_argument(
        "--numguesses", "-n",
        required=False,
        type=int,
        default=gs.NUMGUESSES,
        help="Number of guesses.")

    parser.add_argument(
        "--length", "-l",
        required=False,
        type=int,
        default=gs.WORDLENGTH,
        help="Length of word to guess (omit for random length).")

    parser.add_argument(
        "--wordlist", "-w",
        required=False,
        type=str,
        default=gs.WORDLIST,
        help="Path to file with words (UTF8 encoded).")

    parser.add_argument(
        "--debug", "-d",
        action='store_true',
        help="Debug mode. The answer is 'DEBUG'.")

    args = parser.parse_args(argv[1:])

    return args