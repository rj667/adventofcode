#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    #data = file.read()
    data = [line.strip() for line in file]
    #data = [list(map(str, line.split())) for line in file]

#pprint(data)
numbers = 100
dial = 50
zeroes = 0
for rotation in data:
    if rotation.startswith('L'):
        rotation = rotation.replace('L', '-')
    elif rotation.startswith('R'):
        rotation = rotation.replace('R', '+')
    value = int(rotation)
    full_rotations = value // numbers
    rest_rotation = value - full_rotations * numbers
    dial = (dial + rest_rotation) % numbers
    zeroes
    if dial == 0:
        zeroes += 1

t1 = time.perf_counter()
print(f"Answer: {zeroes}")
print(f"Execution time: {t1 - t0:.6f} seconds")
