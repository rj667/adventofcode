#!/usr/bin/env python3

import sys
import time
import numpy

t0 = time.perf_counter()

infile = sys.argv[0].split('-')[0] + '.input.txt'

total = 0
with open(infile, 'r') as input:
    for line in input:
        game = int(line.split(':', 1)[0].split()[1])
        grabs = line.rstrip().split(':', 1)[1].split(';')
        bag = {'red': 0, 'green': 0, 'blue': 0}
        for grab in grabs:
            cubescolors = grab.split(',')
            for cubescolor in cubescolors:
                cubes, color = cubescolor.strip().split()
                cubes = int(cubes)
                if bag[color] < cubes:
                    bag[color] = cubes
        total += numpy.prod(list(bag.values()))

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
