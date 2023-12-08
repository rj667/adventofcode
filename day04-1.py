#!/usr/bin/env python3

import sys
import time
from pprint import pprint

# This solution works by handling the groups of numbers as sets
# and then finding the intersection. The points are then calculated
# using a power of 2: int(2**(i-1)) produces the range 0,1,2,4,8,..

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0
with open(infile, 'r') as input:
    for line in input:
        winning, having = line.rstrip().split(':')[1].split('|')
        winning = winning.strip().split()
        having = having.strip().split()
        total += int(2 ** (len(set(winning) & set(having)) -1))

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
