#!/usr/bin/env python
import fileinput

total = 0
for line in fileinput.input():
    items = set()
    duplicates = set()
    for item in line[:len(line)//2]:
        items.add(item)
    for item in line[len(line)//2:]:
        if item in items and item not in duplicates:
            if item.isupper():
                total += ord(item) - 64 + 26
            else:
                total += ord(item) - 96
            duplicates.add(item)

print(total)
