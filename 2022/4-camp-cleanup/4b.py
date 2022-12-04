#!/usr/bin/env python
import fileinput

total = 0
for line in fileinput.input():
    assignments = line.split(',')
    bounds = [assignments[0].split('-'), assignments[1].split('-')]
    if (int(bounds[0][0]) <= int(bounds[1][0]) and int(bounds[0][1]) >= int(bounds[1][0])) or (int(bounds[1][0]) <= int(bounds[0][0]) and int(bounds[1][1]) >= int(bounds[0][0])):
        total += 1
print(total)
