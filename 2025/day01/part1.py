#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = [line.strip() for line in file]

#pprint(data)
numbers = 100
dial = 50
zeroes = 0
for line in data:
    direction = line[0]
    distance = int(line[1:])
    if direction == "L":
        dial = numbers if dial == 0 else dial
        zeroes += (numbers - dial + distance) // numbers
        dial = (dial - distance) % numbers
    if direction == "R":
        zeroes += (dial + distance) // numbers
        dial = (dial + distance) % numbers

t1 = time.perf_counter()
print(f"Answer: {zeroes}")
print(f"Execution time: {t1 - t0:.6f} seconds")
