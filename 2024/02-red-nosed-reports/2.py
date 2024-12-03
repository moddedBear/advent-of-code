#!/usr/bin/env python
import sys

def is_safe(levels):
    # a report is safe if:
    # - all levels are either strictly increasing or decreasing
    # - any two adjacent levels differ by between 1 to 3 inclusive
    # a report is also safe if removing one level would fulfil the above rules
    last_diff = None
    for i in range(1, len(levels)):
        diff = levels[i-1] - levels[i]
        # check strictly increasing or decreasing
        if last_diff and diff * last_diff < 0:
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        last_diff = diff
    return True

filename = sys.argv[1]
with open(filename, 'r') as f:
    num_safe = 0
    for report in f:
        levels = report.split()
        levels = [int(level) for level in levels]
        if is_safe(levels):
            num_safe += 1
        else:
            # rerun the safety check with each level removed to see if a safe version exists
            # the length of each report is short enough that this should be fine for performance
            for i in range(len(levels)):
                new_levels = levels.copy()
                new_levels.pop(i)
                if is_safe(new_levels):
                    num_safe += 1
                    break

    print(num_safe)
