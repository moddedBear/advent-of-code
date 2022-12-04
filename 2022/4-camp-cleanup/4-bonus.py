#!/usr/bin/env python
import fileinput

total = 0

# originally i misread the problem and wrote a solution looking for overlapping assignments across the entire input set, not just between pairs
# here's that solution

# first create a sorted array with all assignments
assignments = []
for line in fileinput.input():
    line_assignments = line.split(',')
    for line_assignment in line_assignments:
        bounds = line_assignment.split('-')
        bounds[0] = int(bounds[0])
        bounds[1] = int(bounds[1])
        assignments.append(bounds)
# sort by ascending low bound, descending high bound
assignments.sort(key=lambda x: (x[0], -1 * x[1]))

low = assignments[0][0]
high = assignments[0][1]
for a in assignments[1:]:
    if a[0] >= low and a[1] <= high:
        total += 1
        print(f'{a[0]}, {a[1]} fully contained by {low}, {high}')
    else:
        low = a[0]
        high = a[1]

print(total)
