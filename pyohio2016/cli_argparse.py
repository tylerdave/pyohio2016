#!/usr/bin/env python
from __future__ import print_function

import argparse
import sys
from pyohio2016 import counter

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
            default=sys.stdin, help="Use - to read from stdin.")
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
            default=sys.stdout, help="Optional. By default, writes to stdout.")
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        print("Command args: {0}".format(args), file=sys.stderr)

    text = args.infile.read()
    char_counts = counter.count_chars(text)
    output = "\n".join(["{0} {1}".format(k, v) for k, v in char_counts])
    print(output, file=args.outfile)

if __name__ == '__main__':
    cli()
