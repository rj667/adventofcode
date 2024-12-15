#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
ordering_rules = {}
dependency_count = {}
all_pages = set()
pages_to_produce = []

with open(infile, 'r') as file:
    sections = file.read().split('\n\n', 1)

# parse and process ordering rules
for line in sections[0].splitlines():
    earlier_page, later_page = map(int, line.strip().split("|"))
    if earlier_page not in ordering_rules:
        ordering_rules[earlier_page] = []
    ordering_rules[earlier_page].append(later_page)
    dependency_count[later_page] = dependency_count.get(later_page, 0) + 1
    all_pages.add(earlier_page)
    all_pages.add(later_page)

# add pages without dependency
for page in all_pages:
    if page not in dependency_count:
        dependency_count[page] = 0

print(f'ordering_rules:\n{ordering_rules}')
print(f'dependency_count:\n{dependency_count}')
print(f'all_pages:\n{all_pages}')

# create page ordering
ordered_pages = []
ready_to_print = [page for page in dependency_count if dependency_count[page] == 0]
while ready_to_print:
    current_page = ready_to_print.pop(0)
    ordered_pages.append(current_page)
    if current_page in ordering_rules:
        for dependent_page in ordering_rules[current_page]:
            dependency_count[dependent_page] -= 1
            if dependency_count[dependent_page] == 0:
                ready_to_print.append(dependent_page)
print(f'ordered_pages:\n{ordered_pages}')
# parse pages to produce
for line in sections[1].splitlines():
    pages_to_produce.append(list(map(int, line.split(','))))
print(f'pages_to_produce:\n{pages_to_produce}')

# parse pages to produce
for pages in pages_to_produce:
    if all(ordered_pages.index(x) < ordered_pages.index(y) for x, y in zip(pages, pages[1:])):
        total += pages[len(pages) // 2]

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
