#!/usr/bin/env python3

import re


lines = []
with open('day05.input', 'r') as input:
    for line in input:
        lines.append(tuple(map(int, re.split(',| -> ', line))))

max_x = max(max(x1,x2) for x1,y1,x2,y2 in lines)
max_y = max(max(y1,y2) for x1,y1,x2,y2 in lines)
grid = [[0]*(max_x+1) for i in range(max_y+1)]

for line in lines:
    x1,y1,x2,y2 = line
    #if not (x1 == x2 or y1 == y2): continue
    x = x1
    y = y1
    grid[y][x] += 1
    while not (x == x2 and y == y2):
        if x < x2: x += 1
        if x > x2: x -= 1
        if y < y2: y += 1
        if y > y2: y -= 1
        grid[y][x] += 1

overlap = 0
for row in grid:
    for p in row:
        if p >= 2: overlap+=1

print(f'{overlap} points where at least two lines overlap')
