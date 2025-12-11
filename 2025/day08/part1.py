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

if infile == "input.txt":
    max_connections = 1000
else:
    max_connections = 10

for distance, boxes in sorted(distances)[:max_connections]:
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
    
print(f"Max connections: {max_connections}")
print(f"Number of circuits: {len(circuits)}")
total = math.prod(list(map(len, sorted(circuits, key=len, reverse=True)))[:3])

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
