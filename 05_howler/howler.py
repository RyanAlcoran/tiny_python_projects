#!/usr/bin/env python3
"""
Author : Ryan Alcoran <r.alcoran>
Date   : 2021-01-18
Purpose: Howler
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile
    input_text = ''

    if os.path.isfile(text):
        input_text = open(text).read().rstrip()
    else:
        input_text = text

    if outfile:
        out_fh = open(outfile, 'wt')
        out_fh.write(input_text.upper())
        out_fh.close()
    else:
        print(input_text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
