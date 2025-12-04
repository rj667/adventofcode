#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

h_pos = 0
depth = 0
aim = 0

with open(infile, 'r') as input:
    for line in input:
        (direction, units) = line.split()
        units = int(units)
        if direction == 'down':
            aim += units
        if direction == 'up':
            aim -= units
        if direction == 'forward':
            h_pos += units
            depth += units * aim
        #print(h_pos, depth, aim)

print(f'{h_pos} * {depth} is {h_pos*depth}')
