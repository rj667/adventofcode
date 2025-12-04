#!/usr/bin/env python3

import sys
import time
from pprint import pprint

# This solution reads the input lines and adds dots around the borders.
# Then it loops over the lines char-by-char. If that is a digit, it saves
# it to the current number and checks the 8 surrounding fields for a gear.
# and saves its position. If not, the number is complete and added to the
# list of numbers associated with that position. In the end every position
# with exactly two numbers counts towards the answer.

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0

with open(infile, 'r') as input:
    data = ['.' + line.rstrip() + '.' for line in input]
data.insert(0, '.' * len(data[0]))
data.append('.' * len(data[0]))

number = ''
gear = False
gears = {}
for y in range(1, len(data) -1):
    for x in range(1, len(data[0])):
        if data[y][x].isdigit():
            number += data[y][x]
            if gear:
                continue
            for dy,dx in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                if data[y+dy][x+dx] == '*':
                    gear = (y+dy,x+dx)
        else:
            if number:
                if gear:
                    if gear not in gears:
                         gears[gear] = []
                    gears[gear].append(int(number))
                number = ''
                gear = False

for numbers in gears.values():
    if len(numbers) == 2:
        total += numbers[0] * numbers[1]

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
