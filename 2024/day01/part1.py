#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

list1 = []
list2 = []
total_distance = 0
with open(infile, 'r') as input:
    for line in input:
        loc_id1, loc_id2 = line.split()
        list1.append(int(loc_id1))
        list2.append(int(loc_id2))
    for i in range(len(list1)):
        total_distance += abs(sorted(list1)[i] - sorted(list2)[i])
            

t1 = time.perf_counter()
print(f"Answer: {total_distance}")
print(f"Execution time: {t1 - t0:.6f} seconds")
