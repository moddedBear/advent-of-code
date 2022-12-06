#!/usr/bin/env python
import sys
from collections import deque

filename = sys.argv[1]

# parse stack layout
stacks = None
with open(filename, 'r') as f:
    for line in f:
        if not stacks:
            stacks = [deque() for _ in range(len(line) // 4)]
        if str.isdigit(line[1]):
            break
        for i in range(len(line) // 4):
            crate = line[i*4+1]
            if crate != ' ':
                stacks[i].appendleft(crate)

    # run instructions
    for line in f:
        if line[0] == '\n':
            continue
        line_list = line.split()
        quantity = int(line_list[1])
        from_stack = int(line_list[3]) - 1
        to_stack = int(line_list[5]) - 1
        temp_deque = deque()
        for i in range(quantity):
            temp_deque.append(stacks[from_stack].pop())
        for i in range(quantity):
            stacks[to_stack].append(temp_deque.pop())

# get answer
result = []
for stack in stacks:
    result.append(stack[-1])
result = ''.join(result)
print(result)
