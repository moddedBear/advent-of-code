#!/usr/bin/env python
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    lists = []
    # parse the input and create our lists
    for line in f:
        nums = line.split()
        if not len(lists):  # init the list list
            for _ in nums:
                lists.append([])
        for (i, num) in enumerate(nums):
            lists[i].append(int(num))
    # sort the lists
    for l in lists:
        l.sort()
    # find the total distance
    total = 0
    # I forgot what the problem is so everything up to this point is written for an arbitrary number of lists
    # but here it's hardcoded
    # oh well
    for i in range(len(lists[0])):
        distance = abs(lists[0][i] - lists[1][i])
        total += distance
    
    print(total)