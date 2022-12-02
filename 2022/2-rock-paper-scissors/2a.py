#!/usr/bin/env python
import fileinput

total = 0
for line in fileinput.input():
    # convert plays to their respective point values
    opponent = ord(line[0]) - 64
    me = ord(line[2]) - 87

    if opponent == me:  # draw
        round_score = 3 + me
    elif me - opponent == 1 or me - opponent == -2:  # win
        round_score = 6 + me
    else:  # loss
        round_score = me
    total += round_score

print(total)
