#!/usr/bin/env python3

import sys
import time
from pprint import pprint

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

numbers = {}
parts = []
include = {}
total = 0

with open(infile, 'r') as input:
    y = 0
    for line in input:
        print(f'line: {line.rstrip()}')
        number = ''
        for x, char in enumerate(line):
            #print(f'char: {char}')
            if char.isdigit():
                number += char
            else:
                if number:
                    for pos in range(0, len(number)):
                        numbers[(y,x-pos-1)]= number
                    number = ''
                if char != '.' and char != "\n":
                    parts.append((y,x))
        y += 1

#pprint(numbers)
#pprint(parts)

for part in parts:
    y, x = part
    #print(f'y: {y}, x: {x}')
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            #print((y+dy,x+dx))
            if dy == 0 and dx == 0:
                continue
            if (y+dy,x+dx) in numbers.keys():
                #total += int(numbers[(y+dy,x+dx)])
                #print(f'found: {numbers[(y+dy,x+dx)]}')
                include[numbers[(y+dy,x+dx)]] = True


pprint(include)
for number in include.keys():
    #print(number)
    total += int(number)

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
