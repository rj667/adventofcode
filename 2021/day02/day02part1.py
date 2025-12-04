#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

h_pos = 0
depth = 0

with open(infile, 'r') as input:
    for line in input:
        (direction, units) = line.split()
        units = int(units)
        if direction == 'forward':
            h_pos += units
        if direction == 'down':
            depth += units
        if direction == 'up':
            depth -= units

print(f'{h_pos} * {depth} is {h_pos*depth}')
