# holds the command line argument stuff

import argparse

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

    args = parser.parse_args(argv[1:])

    return args