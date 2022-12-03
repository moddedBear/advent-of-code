#!/usr/bin/env python
import fileinput

total = 0
for line in fileinput.input():
    # convert plays to their respective point values
    total += (((((ord(line[2]) - 89) + (ord(line[0]) - 64 - 1)) + 3) %
              3) + 1) + (ord(line[2]) - 88) * 3

print(total)
