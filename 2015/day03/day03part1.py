#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

from functools import reduce

with open(infile, 'r') as input:
    while True:
        char = input.read(1)
        if not char: break

print(f'output')
