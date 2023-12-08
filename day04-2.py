#!/usr/bin/env python3

import sys
import time
from collections import defaultdict

# This solution works by handling the groups of numbers as sets
# and then finding the intersection. The number of copies is
# maintained in a defaultdict so that by default value 0 is assumed.
# Then the answer is just the sum of the number of copies.

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0
cards = []
copies = defaultdict(int)
with open(infile, 'r') as input:
    card = 0
    for line in input:
        card += 1
        copies[card] += 1
        winning, having = line.rstrip().split(':')[1].split('|')
        winning = winning.strip().split()
        having = having.strip().split()
        matches = len(set(winning) & set(having))
        for copy in range(copies[card]):
            for num in range(1, matches + 1):
                copies[card + num] += 1

total = sum(copies.values())
t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
