#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import math

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    lines = [line.strip() for line in file]
    operators = list(map(str, lines.pop().split()))
    data = [list(map(int, line.split())) for line in lines]

for x in range(len(data[0])):
    numbers = []
    for y in range(len(data)):
        numbers.append(data[y][x])
    if operators[x] == "+":
        total += sum(numbers)
    elif operators[x] == "*":
        total += math.prod(numbers)

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
