#!/usr/bin/env python
import sys
import heapq

RESULT_SIZE = 3
filename = sys.argv[1]

highest = [0] * RESULT_SIZE
heapq.heapify(highest)
current = 0
with open(filename, 'r') as f:
    for line in f:
        if line == '\n':
            heapq.heappushpop(highest, current)
            current = 0
        else:
            current += int(line)
    heapq.heappushpop(highest, current)
result = 0
for num in highest:
    result += num
print(highest)
print(result)
