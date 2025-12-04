#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = [line.strip() for line in file]

needed = 12

for line in data:
    bank = list(map(int, list(line)))
    #print(f'BANK: {bank}')
    joltage = ""
    pos = -1
    for n in range(needed):
        select_from = bank[pos+1:len(bank)-needed+n+1]
        battery = max(select_from)
        joltage += str(battery)
        #print(f"      {select_from}, battery: {battery}, joltage: {joltage}")
        pos = bank.index(battery, pos+1)
    total += int(joltage)

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
