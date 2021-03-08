#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2021-01-24
Purpose: Rock the Casbah
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u'])
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(text).read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    output_text = ''
    for char in args.text:
        if char in 'aeiou':
            output_text += args.vowel
        elif char in 'AEIOU':
            output_text += args.vowel.upper()
        else: 
            output_text += char
    print(output_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
