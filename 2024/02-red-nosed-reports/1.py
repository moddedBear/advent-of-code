#!/usr/bin/env python
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    num_safe = 0
    for report in f:
        # a report is safe if:
        # - all levels are either strictly increasing or decreasing
        # - any two adjacent levels differ by between 1 to 3 inclusive
        is_safe = True
        levels = report.split()
        levels = [int(level) for level in levels]
        last_diff = None
        for i in range(1, len(levels)):
            diff = levels[i-1] - levels[i]
            # check strictly increasing or decreasing
            if last_diff and diff * last_diff < 0:
                is_safe = False
            if abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
            last_diff = diff
        if is_safe:
            num_safe += 1

    print(num_safe)