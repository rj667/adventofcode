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
        if line[0] == '#': continue
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
    print('input_range: ', input_range)
    print('compare_ranges: ', pformat(compare_ranges))
    output_ranges = []
    input_start, input_length = input_range
    for compare_range in compare_ranges:
        input_range = [input_start, input_length]
        input_end = input_start + input_length - 1
        print(f'input range: {input_range} = {input_start}-{input_end}')
        compare_dest, compare_start, compare_length = compare_range
        compare_end = compare_start + compare_length - 1
        print(f'compare range: {compare_range} = {compare_start}-{compare_end}')
        if input_start >= compare_start and input_start < compare_start + compare_length:
            # input start is in range
            print('input start IS in range')
            if input_start + input_length <= compare_start + compare_length:
                # input end is in range
                print('input end IS in range')
                new_range = [input_start + (compare_dest - compare_start), input_length]
                print('transformed whole range:', new_range)
                output_ranges.append(new_range)
                input_start = input_start + input_length
                input_length = input_length - compare_length
                break
            else:
                print('input end IS NOT in range')
                new_range = [input_start + (compare_dest - compare_start), compare_length]
                print('transformed partial range: ', new_range)
                output_ranges.append(new_range)
                rest_range = (input_start + (compare_dest - compare_start - 1), input_length - compare_length)
                print('rest range:', rest_range)
                input_start, input_length = rest_range
        else:
            # skip range
            print('input start IS NOT in range: SKIPPING')
            continue
    else:
        if input_length > 0:
            print('else range:', [input_start, input_length])
            output_ranges.append([input_start, input_length])
    print('output_ranges:', output_ranges)
    return output_ranges


seeds = list(zip(seeds[::2], seeds[1::2]))
result_ranges = []
for seed_start, seed_length in seeds:
    ranges_todo = [[seed_start, seed_length]]
    for map_name in mapnames:
        print('BEGIN MAP:', map_name, 'ranges_todo', ranges_todo)
        ranges_done = []
        for range_todo in ranges_todo:
            ranges_done += src_to_dest(range_todo, mapranges[map_name])
        print('END MAP:', map_name, 'ranges_done', pformat(ranges_done))
        ranges_todo = ranges_done
    result_ranges += ranges_done

print('result_ranges:', pformat(result_ranges))
answer = min([result_range[0] for result_range in result_ranges])



t1 = time.perf_counter()
print(f"Answer: {answer}")
print(f"Execution time: {t1 - t0:.6f} seconds")
