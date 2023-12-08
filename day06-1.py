#!/usr/bin/env python3

import sys
import time
from pprint import pprint

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0
with open(infile, 'r') as input:
    durations = list(map(int, input.readline().split(':')[1].strip().split()))
    distances = list(map(int, input.readline().split(':')[1].strip().split()))
pprint(durations)
pprint(distances)

for race, duration in enumerate(durations):
    distance = distances[race]
    print(race, duration, distance)
    delta = distance - duration
    print(f'delta: {delta}')
    print(sum(list(range(delta, duration - delta))))

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
