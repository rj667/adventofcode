#!/usr/bin/env python3

import sys
import time

t0 = time.time()

infile = sys.argv[0].split('-')[0] + '.input.txt'
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
total = 0

with open(infile, 'r') as input:
    for line in input:
        digits = []
        for i in range(0, len(line.rstrip())):
            if line[i].isdigit():
                digits.append(line[i])
                continue
            for j in range(1, len(words)):
                if line[i:].startswith(words[j]):
                    digits.append(str(j))
                    continue
        number = int(digits[0] + digits[-1])
        total += number

t1 = time.time()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.2f} seconds")
