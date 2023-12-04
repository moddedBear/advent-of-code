#!/usr/bin/env python
import sys
import re

# need to find all gears (*s which is adjacent to EXACTLY two part numbers)
# find gear ratio of each gear (two numbers multiplied)
# add all gear ratios for result
DIGIT_PATTERN = r'\d+'
SYMBOL_PATTERN = r'(?=\W)[^.]'
GEAR_PATTERN = r'\*'

# returns a list of all numbers adjacent to a gear
def get_nums(gear_pos, check_lines):
    start = max(gear_pos - 1, 0)
    end = min(gear_pos + 1, len(check_lines[0]) - 1)
    nums = []
    for line in check_lines:
        if line:
            matches = re.finditer(DIGIT_PATTERN, line)
            for match in matches:
                if start <= match.start() <= end or start <= match.end() - 1 <= end:
                    nums.append(match[0])
    return nums

filename = sys.argv[1]
result = 0
with open(filename, 'r') as input:
    lines = input.readlines()

for line_index, line in enumerate(lines):
    prev_line = lines[line_index - 1] if line_index > 0 else None
    next_line = lines[line_index + 1] if line_index < len(lines) - 1 else None
    to_check = [prev_line, line, next_line]
    gears = re.finditer(GEAR_PATTERN, line)
    for gear_match in gears:
        parts = get_nums(gear_match.start(), to_check)
        if len(parts) == 2:
            result += int(parts[0]) * int(parts[1])

print(result)
