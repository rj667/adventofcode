#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

floor = 0

with open(infile, 'r') as input:
    while True:
        char = input.read(1)
        if not char: break
        if char == '(': floor+=1
        if char == ')': floor-=1

print(f'floor: {floor}')
