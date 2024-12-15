#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import re

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0
with open(infile, 'r') as file:
    memory = file.read()
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    for match in re.finditer(pattern, memory):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total += num1 * num2

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
