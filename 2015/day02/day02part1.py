#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'


total_wrap = 0

with open(infile, 'r') as input:
    for line in input:
        (l,w,h) = map(int, line.rstrip('\n').split('x'))
        wrap = 2*l*w + 2*w*h + 2*h*l + min((l*w,w*h,h*l))
        print((l,w,h), wrap)
        total_wrap += wrap

print(f'square feet of wrapping paper: {total_wrap}')
