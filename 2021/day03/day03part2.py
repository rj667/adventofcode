#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

def nbit_set(x, n):
    return x & (1 << (n - 1))

bits = 0
oxy = []
co2 = []

with open(infile, 'r') as input:
    for line in input:
        if not bits: bits = len(line.strip())
        oxy.append(int(line, 2))
        co2.append(int(line, 2))

for n in range(bits, 0, -1):
    tmp = list(filter(lambda x: nbit_set(x, n), oxy))
    if len(tmp)*2 < len(oxy):
        tmp = list(filter(lambda x: not nbit_set(x, n), oxy))
    oxy = tmp
    if len(oxy) == 1: break

for n in range(bits, 0, -1):
    tmp = list(filter(lambda x: nbit_set(x, n), co2))
    if len(tmp)*2 >= len(co2):
        tmp = list(filter(lambda x: not nbit_set(x, n), co2))
    co2 = tmp
    if len(co2) == 1: break

print(f'{oxy[0]} * {co2[0]} = {oxy[0] * co2[0]} is life support rating')
