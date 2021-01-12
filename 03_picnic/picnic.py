#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2021-01-11
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    length = len(args.item)
    if args.sorted:
        items = sorted(args.item)
    else:
        items = args.item

    if length >= 2:
        items.insert(-1, 'and')
    
    if length > 2:
        print(f"You are bringing {', '.join(items[:-1])} {items[-1]}.") 
    else:
        print(f"You are bringing {' '.join(items)}.")

# --------------------------------------------------
if __name__ == '__main__':
    main()
