#!/usr/bin/env python3

from statistics import median

with open('day07.input', 'r') as input:
    crabs = list(map(int, input.readline().split(',')))

#print(crabs)
pos = median(crabs)
fuel = sum(abs(pos-crab) for crab in crabs)
print(f'{fuel} fuel to align to position {pos}')
