#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2021-03-22
Purpose: Ransom
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int)
    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args

# --------------------------------------------------
def choose(char): return random.choice([char.lower(), char.upper()])

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    output = ''
    for char in args.text:
        output += choose(char)
    print(output)
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
