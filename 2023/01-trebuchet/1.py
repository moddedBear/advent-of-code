#!/usr/bin/env python
import sys
import re

filename = sys.argv[1]
with open(filename, 'r') as f:
    pattern = r"\d"
    result = 0
    for line in f:
        matches = re.findall(pattern, line)
        if len(matches):
            result += int(matches[0] + matches[-1])

print(result)
