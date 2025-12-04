#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = [line.strip() for line in file]

for line in data:
    bank = list(map(int, list(line)))
    bat1 = max(bank[:len(bank)-1])
    pos1 = bank.index(bat1)
    bat2 = max(bank[pos1+1:])
    joltage = int(str(bat1) + str(bat2))
    total += joltage

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
