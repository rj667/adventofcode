#!/usr/bin/env python3

import sys
import time

# This implementation just loops over each grab of each game
# and determines if the game is valid.
# It has some not very intuitive code to break the outer loop
# from the inner loop, hence the comments.

t0 = time.perf_counter()

infile = sys.argv[0].split('-')[0] + '.input.txt'
bag = {'red': 12, 'green': 13, 'blue': 14}

total = 0
with open(infile, 'r') as input:
    for line in input:
        game = int(line.split(':', 1)[0].split()[1])
        grabs = line.rstrip().split(':', 1)[1].split(';')
        for grab in grabs:
            cubescolors = grab.split(',')
            for cubescolor in cubescolors:
                cubes, color = cubescolor.strip().split()
                cubes = int(cubes)
                if cubes > bag[color]:
                    break
            else:
                # the inner loop did not break
                continue
            # the inner loop did break
            break
        else:
            # the outer loop did not break
            total += game

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
