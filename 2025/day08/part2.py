#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import math

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    boxes = [tuple(map(int, line.split(","))) for line in file]
#pprint(boxes)

seen_boxes = []
distances = []
circuits = []
for box in boxes:
    for seen in seen_boxes:
        distance = math.sqrt(abs(seen[0]-box[0])**2 + abs(seen[1]-box[1])**2 + abs(seen[2]-box[2])**2)
        distances.append((distance, set([seen, box])))
    seen_boxes.append(box)
    circuits.append([box])
distances.sort()

#pprint(distances)
#pprint(circuits)

for distance, boxes in sorted(distances):
    box1, box2 = boxes
    #print(f"Connecting {box1} and {box2} with distance {distance}")
    circuit1 = None
    circuit2 = None
    for circuit in circuits:
        #print(f"Checking circuit: {circuit}")
        try:
            circuit.index(box1)
            circuit1 = circuit
        except ValueError:
            pass
        try:
            circuit.index(box2)
            circuit2 = circuit
        except ValueError:
            pass

    if circuit1 != circuit2:
        circuits.remove(circuit1)
        circuits.remove(circuit2)
        circuits.append(circuit1+circuit2)
        if len(circuits) == 1:
            print(f"box1: {box1}, box2: {box2}")
            total = box1[0] * box2[0]
            break

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
