#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2021-01-13
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    jumper = {'1' : '9', '2' : '8', '3' : '7', '4' : '6', '5' : '0',
              '6' : '4', '7' : '3', '8' : '2', '9' : '1', '0' : '5'}
    args = get_args()
    input_text = args.text
    """
    Original Solution:
    for char in input_text:
        if jumper.get(char, 'NA') == 'NA':
            print(char, end='')
        else:
            print(jumper.get(char), end='')
    print()
    """
    # Solution from exercise
    for char in input_text:
        print(jumper.get(char, char), end='')
    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
