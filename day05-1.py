#!/usr/bin/env python3

import sys
import time

# This solution works by remembering the map names and order while reading the input
# and then for each sead calling the mapping function for each of the map name in the list.

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()


def get_map_value(number, ranges):
    for dest, source, length in ranges:
        if source <= number < source + length:
            return dest + number - source
    return number
    

maps = {}
mapnames = []
with open(infile, 'r') as input:
    seeds = list(map(int, input.readline().rstrip().split(':')[1].strip().split()))
    for line in input:
        if not line.rstrip():
            mapname = input.readline().rstrip().split()[0].split('-')[-1]
            mapnames.append(mapname)
            continue
        if mapname not in maps:
            maps[mapname] = []
        maps[mapname].append(list(map(int, line.rstrip().split())))

numbers = []
for seed in seeds:
    number = seed
    for mapname in mapnames:
        number = get_map_value(number, maps[mapname])
    numbers.append(number)

answer = min(numbers)

t1 = time.perf_counter()
print(f"Answer: {answer}")
print(f"Execution time: {t1 - t0:.6f} seconds")
