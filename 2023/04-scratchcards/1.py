#!/usr/bin/env python
import sys
import re

# first section is winning numbers
# second section is numbers we have
# a card's value becomes 1 with the first match, then doubles for each after that
# find total value

filename = sys.argv[1]
result = 0
with open(filename, 'r') as input:
    for line in input:
        value = 0
        # split the line into sections and then numbers
        _, winning_nums, our_nums = re.split(r':|\|', line)
        winning_nums = winning_nums.split()
        our_nums = our_nums.split()
        for num in our_nums:
            if num in winning_nums:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        result += value
print(result)
