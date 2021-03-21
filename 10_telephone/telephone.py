#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2021-03-08
Purpose: 10_telephone
"""

import argparse
import random
import os
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=.1)

    args = parser.parse_args()
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    if ((args.mutations < 0) or (args.mutations > 1)):
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    num_mutations = round(len(args.text) * args.mutations)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    text = args.text
    indexes = random.sample(range(len(text)), num_mutations)
    result = text
    """
    print(f'alpha: {alpha}')
    print(f'indexes: {indexes}')
    for i in indexes:
        print(f'{i:2} {text[i]}')
    """
    for i in indexes:
        result = result[:i] + random.choice(alpha.replace(result[i],'')) + result[i+1:]
    print(f'You said: "{text}"')
    print(f'I heard: "{result}"')
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
