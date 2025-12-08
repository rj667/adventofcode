#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import math

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = [line.rstrip("\n")+" " for line in file]

numbers = []
operator = None
for x in range(len(data[0])):
    number = ""
    for y in range(len(data)-1):
        number += data[y][x]
    if number.isspace():
        if operator == '+':
            total += sum(numbers)
        elif operator == '*':
            total += math.prod(numbers)
        numbers = []
        operator = None
        continue
    else:
        numbers.append(int(number))
    if operator is None:
        operator = data[len(data)-1][x]

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
