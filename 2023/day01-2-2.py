#!/usr/bin/env python3

import sys
import time

t0 = time.perf_counter()
infile = sys.argv[0].split('-')[0] + '.input.txt'

# Another implementation that works by finding the first occurence of all
# (spelled out) digits in the line. This results in a dict with starting positions
# and with spelled out digits already mapped. After -1 (not found) is dropped,
# the value with the lowest key is the first found digit.
# This is repeated for the reversed line with reversed words.

words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reversed_words = list(map(lambda x: ''.join(reversed(x)), words))
digits = list(map(str, range(len(words))))
total = 0

with open(infile, 'r') as input:
    for line in input:
        line = line.rstrip()
        value = ''
        for line in line, ''.join(reversed(line)):
            d = dict(zip(list(map(line.find, words + digits)), digits + digits))
            d.pop(-1)
            value += d[min(d.keys())]
            words, reversed_words = reversed_words, words
        total += int(value)


t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
