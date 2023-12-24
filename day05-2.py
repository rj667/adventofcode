#!/usr/bin/env python3

import sys
import time
from pprint import pformat

# This brute-force solution takes too long...

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()


def get_map_value(number, ranges):
    for dest, source, length in ranges:
        if source <= number < source + length:
            return dest + number - source
    return number
    

mapranges = {}
mapnames = []
with open(infile, 'r') as input:
    seeds = list(map(int, input.readline().rstrip().split(':')[1].strip().split()))
    for line in input:
        # read map name
        if not line.rstrip():
            name = input.readline().rstrip().split()[0].split('-')[-1]
            mapnames.append(name)
            mapranges[name] = []
            continue
        # read ranges
        mapranges[name].append(list(map(int, line.rstrip().split())))
print('seeds:', seeds)

# sort ranges in each map 
for name in mapnames:
    mapranges[name].sort(key = lambda x: x[1])
    # if needed, insert a range starting at zero
    if mapranges[name][0][1] != 0:
        mapranges[name].insert(0, [0,0,mapranges[name][0][1]])
print("mapranges:\n", pformat(mapranges, sort_dicts=False))

def src_to_dest (input_range, compare_ranges):
    output_ranges = []
    input_start, input_length = input_range
    for range_dest, range_start, range_length in compare_ranges:
        print('input range:', (input_start, input_length))
        print('compare range:', (range_start, range_length))
        if input_start >= range_start and input_start < range_start + range_length:
            # input start is in range
            print('input start IS in range')
            if input_start + input_length <= range_start + range_length:
                # input end is in range
                print('input end IS in range')
                new_range = (input_start + (range_dest - range_start), input_length)
                print('new range:', new_range)
                #output_ranges.append((input_start + (range_dest - range_start), input_length))
                output_ranges.append(new_range)
                break
            else:
                print('input end IS NOT in range')
                new_range = (input_start + (range_dest - range_start), range_length)
                print('new range:', new_range)
                #output_ranges.append((input_start + (range_dest - range_start), range_length))
                output_ranges.append(new_range)
                input_start += range_length
                input_length -= range_length
                print('new range:', (input_start, input_length))
        else:
            # skip range
            print('input start IS NOT in range: SKIPPING')
            continue
    else:
        print('rest range:', (input_start, input_length))
        output_ranges.append((input_start, input_length))
    print('output_ranges:', output_ranges)
    return output_ranges


ranges_todo = list(zip(seeds[::2], seeds[1::2]))
for map_name in mapnames:
    print('MAP:', map_name, 'ranges_todo', pformat(ranges_todo))
    ranges_done = []
    for range_todo in ranges_todo:
        ranges_done += src_to_dest(range_todo, mapranges[map_name])
    print('MAP:', map_name, 'ranges_done', pformat(ranges_done))
    ranges_todo = ranges_done

print('ranges_todo:', ranges_todo)


answer = 0

t1 = time.perf_counter()
print(f"Answer: {answer}")
print(f"Execution time: {t1 - t0:.6f} seconds")
