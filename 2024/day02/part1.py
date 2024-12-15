#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import operator

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

def is_decreasing(mylist):
    return all(x > y for x, y in zip(mylist, mylist[1:]))

def is_increasing(mylist):
    return all(x < y for x, y in zip(mylist, mylist[1:]))

def is_near(mylist):
    return all(abs(x-y) <= 3 for x, y in zip(mylist, mylist[1:]))

def is_safe(mylist):
    return (is_decreasing(mylist) or is_increasing(mylist)) and is_near(mylist)

safe_reports = 0
with open(infile, 'r') as my_input:
    reports = [list(map(int, line.split())) for line in my_input]

for levels in reports:
    #print(levels)
    if is_safe(levels):
        safe_reports += 1
    else:
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i+1:]
            if is_safe(new_levels):
                safe_reports += 1
                break

t1 = time.perf_counter()
print(f"Answer: {safe_reports}")
print(f"Execution time: {t1 - t0:.6f} seconds")
