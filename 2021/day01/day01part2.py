#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

inc = 0
q = []
winsize = 3
maxqsize = winsize + 1
with open(infile, 'r') as input:
    for line in input:
        depth=int(line)
        q.append(depth)
        if len(q) > maxqsize:
            q.pop(0)
        if len(q) == maxqsize:
            win1 = q[0:winsize]
            win2 = q[1:winsize+1]
            print(q, win1, win2, sum(win1), sum(win2) )
            if sum(win2) > sum(win1):
                inc += 1
print(f'{inc} measurements are larger than the previous measurement')
