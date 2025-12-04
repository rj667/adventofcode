#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'


total_ribbon = 0

with open(infile, 'r') as input:
    for line in input:
        l,w,h = map(int, line.split('x'))
        dim = [l,w,h]
        dim.sort()
        dim.pop()
        x,y = dim
        total_ribbon += x+x+y+y + l*w*h

print(f'{total_ribbon} feet of ribbon paper')
