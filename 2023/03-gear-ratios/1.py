#!/usr/bin/env python
import sys
import re

# need to add all numbers adjacent to a symbol, even diagonally
DIGIT_PATTERN = r'\d+'
SYMBOL_PATTERN = r'(?=\W)[^.]'

def has_symbol(line, start, end):
    start = max(start, 0)
    end = min(end, len(line) - 1)
    if re.search(SYMBOL_PATTERN, line[start:end]):
        return True
    return False

filename = sys.argv[1]
result = 0
with open(filename, 'r') as input:
    lines = input.readlines()

for line_index, line in enumerate(lines):
    prev_line = lines[line_index - 1] if line_index > 0 else None
    next_line = lines[line_index + 1] if line_index < len(lines) - 1 else None
    to_check = [prev_line, line, next_line]
    numbers = re.finditer(DIGIT_PATTERN, line)
    for number_match in numbers:
        number = number_match[0]
        start_col, end_col = number_match.start(), number_match.end()
        for check_line in to_check:
            if check_line:
                if has_symbol(check_line, start_col - 1, end_col + 1):
                    result += int(number)
                    continue

print(result)
