#!/usr/bin/env python
import sys
import re

filename = sys.argv[1]
mul_pattern = r'mul\((\d+),(\d+)\)'
result = 0
with open(filename, 'r') as f:
    # oh boy regex
    matches = re.findall(mul_pattern, f.read())
    for match in matches:
        (a, b) = match
        result += int(a) * int(b)
    print(result)