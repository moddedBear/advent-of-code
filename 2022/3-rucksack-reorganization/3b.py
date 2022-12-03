#!/usr/bin/env python
import sys

filename = sys.argv[1]
total = 0
with open(filename) as f:
    for line_1 in f:
        line_2 = next(f)
        line_3 = next(f)
        lines = [line_1, line_2, line_3]
        items = [set(), set(), set()]
        for i, line in enumerate(lines):
            for item in line:
                if item != '\n':
                    items[i].add(item)
        badge = next(iter((items[0].intersection(items[1], items[2]))))
        if badge.isupper():
            total += ord(badge) - 64 + 26
        else:
            total += ord(badge) - 96

print(total)
