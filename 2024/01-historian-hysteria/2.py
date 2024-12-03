#!/usr/bin/env python
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    occurences = {}
    left = []
    right = []
    # parse the input and create our lists
    for line in f:
        nums = line.split()
        # add left value
        left.append(int(nums[0]))
        # add right value
        if int(nums[1]) not in occurences:
            occurences[int(nums[1])] = 1
        else:
            occurences[int(nums[1])] += 1
        right.append(int(nums[1]))
    
    # find the similarity score
    # similarity = key * value
    total = 0
    for num in left:
        if num in occurences:
            total += num * occurences[num]
    print(total)