#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

with open(infile, 'r') as input:
    for line in input:
        print(line)
print(f'output')
