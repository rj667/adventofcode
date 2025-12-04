#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

prev_depth = None
inc = 0

with open(infile, 'r') as input:
    for line in input:
        depth=int(line)
        try:
            if depth > prev_depth:
                inc += 1
        except TypeError:
            pass
        prev_depth = depth
print(f'{inc} measurements are larger than the previous measurement')
