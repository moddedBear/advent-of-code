#!/usr/bin/env python
import fileinput
from collections import deque

dirs = dict()
dir_stack = deque()
for line in fileinput.input():
    words = line.strip().split(' ')
    if words[0] == '$':
        if words[1] == 'cd':
            d = words[2]
            wd = str.join('/', dir_stack) + d
            if d == '..':
                dir_stack.pop()
            else:
                if wd not in dirs:
                    dirs[wd] = 0
                dir_stack.append(wd)
    elif words[0] != 'dir':
        size = int(words[0])
        for d in dir_stack:
            dirs[d] += size

space_to_free = 30000000 - (70000000 - dirs['/'])
candidates = [v for (_, v) in dirs.items() if v >= space_to_free]
result = min(candidates)
print(result)
