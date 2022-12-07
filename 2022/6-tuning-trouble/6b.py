#!/usr/bin/env python
import fileinput


for line in fileinput.input():
    beginning = 13
    for i in range(len(line)):
        beginning += 1
        lookback = line[i: i+14]
        if len(set(lookback)) == 14:
            print(beginning)
            break
