#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

list1 = []
list2 = []
similarity_score = 0
with open(infile, 'r') as input:
    for line in input:
        loc_id1, loc_id2 = line.split()
        list1.append(int(loc_id1))
        list2.append(int(loc_id2))
    for loc_id1 in list1:
        similarity_score += loc_id1 * list2.count(loc_id1)
            

t1 = time.perf_counter()
print(f"Answer: {similarity_score}")
print(f"Execution time: {t1 - t0:.6f} seconds")
