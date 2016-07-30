#!/usr/bin/env python
"""Hello, Docopt.

Usage:
  hello-docopt <name>
  hello-docopt [--count=<int>] <name>
  hello-docopt -h | --help

Options:
  -h --help          Show this screen.
  -c --count=<int>   Times to print greeting [default: 1].
"""
from docopt import docopt

def hello():
    args=docopt(__doc__)
    for i in xrange(int(args['--count'])):
        print("Hello, {0}!".format(args['<name>']))

if __name__ == '__main__':
    hello()
