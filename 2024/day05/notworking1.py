#!/usr/bin/env python3

import sys
import time
from pprint import pprint

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0
with open(infile, 'r') as file:
    data = file.read().strip()
    sections = data.split('\n\n')
    page_ordering_rules = sections[0].splitlines()
    pages_to_produce = sections[1].splitlines() if len(sections) > 1 else []

# parse page ordering rules
page_ordering_rules = [list(map(int, rule.split('|'))) for rule in page_ordering_rules]
page_ordering_rules = sorted(page_ordering_rules, key=lambda x: (x[1], x[0]))
print(page_ordering_rules)

# create page ordering
page_ordering = []
for first, second in page_ordering_rules:
    if second not in page_ordering:
        page_ordering.append(second)
    if first not in page_ordering:
        page_ordering.insert(page_ordering.index(second), first)
    if page_ordering.index(first) > page_ordering.index(second):
        page_ordering.remove(first)
        page_ordering.insert(page_ordering.index(second), first)
print(page_ordering)

# parse pages to produce
pages_to_produce = [list(map(int, pages.split(','))) for pages in pages_to_produce]
for pages in pages_to_produce:
    print(pages)
    if all(page_ordering.index(x) < page_ordering.index(y) for x, y in zip(pages, pages[1:])):
        print("yes")
        total += pages[len(pages) // 2]

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
