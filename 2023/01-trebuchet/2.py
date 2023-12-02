#!/usr/bin/env python
import sys
import re

str2int = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
        }
filename = sys.argv[1]
with open(filename, 'r') as f:
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    result = 0
    for line in f:
        matches = re.findall(pattern, line)
        if len(matches):
            first = str2int[matches[0]] if matches[0] in str2int else matches[0]
            last = str2int[matches[-1]] if matches[-1] in str2int else matches[-1]
            result += int(first + last)

print(result)
