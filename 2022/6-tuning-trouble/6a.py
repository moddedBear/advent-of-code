#!/usr/bin/env python
import fileinput
from collections import deque


for line in fileinput.input():
    beginning = 0
    lookback = deque()
    for c in line:
        beginning += 1
        if len(lookback) > 3:
            lookback.popleft()
        lookback.append(c)
        if len(lookback) == len(set(lookback)) == 4:
            print(beginning)
            break
