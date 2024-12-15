#!/usr/bin/env python3

import sys
import time
from pprint import pprint

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            stone_string = str(stone)
            if not len(stone_string) % 2:
                half_length = int(len(stone_string) / 2)
                #print([int(stone_string[0:half_length]), int(stone_string[half_length:])])
                new_stones.extend([int(stone_string[0:half_length]), int(stone_string[half_length:])])
            else:
                new_stones.append(stone * 2024)
    return new_stones

total = 0
with open(infile, 'r') as file:
    stones = list(map(int, file.readline().split()))

print(stones)
for n in range(25):
    stones = blink(stones)
    total = len(stones)
    print(n+1, total)

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
