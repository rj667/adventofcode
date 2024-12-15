#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import re

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

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
