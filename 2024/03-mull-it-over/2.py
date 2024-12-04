#!/usr/bin/env python
import sys
import re

filename = sys.argv[1]
mul_pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
result = 0
with open(filename, 'r') as f:
    # oh boy regex
    matches = re.findall(mul_pattern, f.read())
    # print(matches)
    doing = True
    for match in matches:
        (a, b, do, dont) = match
        if do:
            doing = True
        elif dont:
            doing = False
        elif a and b and doing:
            result += int(a) * int(b)
    print(result)