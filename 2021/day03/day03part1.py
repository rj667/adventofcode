#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

bits = []

with open(infile, 'r') as input:
    lines = 0
    for line in input:
        pos = 0
        for c in line.rstrip():
            try:
                bits[pos] += int(c)
            except IndexError:
                bits.append(int(c))
            pos += 1
        lines += 1

gamma = '0b'
for n in bits:
    if n*2 > lines:
        gamma += '1'
    else:
        gamma += '0'

gamma = int(gamma, 2)
epsilon = gamma ^ int('0b' + '1' * len(bits), 2)

print(f'{gamma} * {epsilon} = {gamma * epsilon} is the power consumption')
