#!/usr/bin/env python3

import sys
import time
from pprint import pprint
from collections import Counter, defaultdict

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

def blink(stones):
    new_stones = defaultdict(int)
    for stone in stones.keys():
        if stone == 0:
            new_stones[1] += stones[0]
        else:
            stone_string = str(stone)
            if not len(stone_string) % 2:
                middle = len(stone_string) // 2
                new_stone1 = int(stone_string[:middle])
                new_stone2 = int(stone_string[middle:])
                new_stones[new_stone1] += stones[stone]
                new_stones[new_stone2] += stones[stone]
            else:
                new_stones[stone * 2024] += stones[stone]
    return new_stones

total = 0
with open(infile, 'r') as file:
    stones = Counter(list(map(int, file.readline().split())))

for n in range(75):
    stones = blink(stones)

total = sum(stones.values())
t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
