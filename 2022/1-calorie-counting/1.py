#!/usr/bin/env python
import sys


filename = sys.argv[1]
result = 0
current = 0
with open(filename, 'r') as f:
    for line in f:
        if line == '\n':
            if current > result:
                result = current
            current = 0
        else:
            current += int(line)
    if current > result:
        result = current
print(result)
