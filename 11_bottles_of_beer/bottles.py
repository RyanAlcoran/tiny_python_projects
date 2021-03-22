#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2021-03-22
Purpose: 11_Bottles
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many Bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def verse(num):
    if num > 2:
        bottle = 'bottles'
        next_bottle = f'{num - 1} bottles'
    elif num == 2:
        bottle = 'bottles'
        next_bottle = f'1 bottle'
    else:
        bottle = 'bottle'
        next_bottle = f'No more bottles'
    l1 = f'{num} {bottle} of beer on the wall,\n'
    l2 = f'{num} {bottle} of beer,\n'
    l3 = f'Take one down, pass it around,\n'
    l4 = f'{next_bottle} of beer on the wall!'
    
    return l1 + l2 + l3 + l4


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
        ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
        ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number = args.num 
    for i in list(range(number, 0, -1)):
        print(verse(i), end='\n' * (2 if i > 1 else 1))


# --------------------------------------------------
if __name__ == '__main__':
    main()
