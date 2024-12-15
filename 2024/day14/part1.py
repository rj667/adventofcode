#!/usr/bin/env python3

import sys
import time
import re

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0

def visualise(robots):
    grid = grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for robot in robots:
        x,y,dx,dy = robot
        if grid[y][x] == '.':
            grid[y][x] = '1'
        else:
            grid[y][x] = str(int(grid[y][x]) + 1)
    print('\n'.join(''.join(row) for row in grid) + '\n')

def move(robots):
    for i,robot in enumerate(robots):
        x,y,dx,dy = robot
        x = (x + dx) % max_x
        y = (y + dy) % max_y
        robots[i] = [x,y,dx,dy]
    return robots

def calc_safety(robots):
    Q = [0,0,0,0]
    for robot in robots:
        x,y,dx,dy = robot
        if x < max_x // 2 and y < max_y // 2: Q[0] += 1
        if x > max_x // 2 and y < max_y // 2: Q[1] += 1
        if x < max_x // 2 and y > max_y // 2: Q[2] += 1
        if x > max_x // 2 and y > max_y // 2: Q[3] += 1
    return Q[0] * Q[1] * Q[2] * Q[3]

robots = []
max_x = max_y = 0
with open(infile, 'r') as file:
    for line in file:
        x,y,dx,dy = list(map(int, re.findall(r'-?\d+', line)))
        robots.append([x,y,dx,dy])
    max_x = max(robot[0] for robot in robots) + 1
    max_y = max(robot[1] for robot in robots) + 1
    #visualise(robots)

for seconds in range(100):
    print(f"seconds: {seconds+1}")
    robots = move(robots)
    #visualise(robots)

total = calc_safety(robots)

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
