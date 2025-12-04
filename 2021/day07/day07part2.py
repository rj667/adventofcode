#!/usr/bin/env python3

with open('day07.example', 'r') as input:
    crabs = list(map(int, input.readline().split(',')))

avg = sum(crabs)/len(crabs)
smaller = [crab < avg for crab in crabs]
if smaller.count(True) < smaller.count(False):
    avg = int(avg)
else:
    avg = int(avg+1)

#print(crabs)
fuel = sum(sum(range(abs(crab-avg)+1)) for crab in crabs)
print(f'{fuel} fuel to align to position {avg}')

# 92439832 fuel to align to position 458
