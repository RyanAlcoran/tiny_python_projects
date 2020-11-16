#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2020-11-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    return parser.parse_args()

# --------------------------------------------------
def is_vowel(char):
    """Check if character is a vowel"""

    ch = char.lower()
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        return True
    else:
        return False

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = ''
    if (is_vowel(word[0]) == True):
        article = 'an '
    else:
        article = 'a '
    print('Ahoy, Captain, '+ article + word + ' off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
