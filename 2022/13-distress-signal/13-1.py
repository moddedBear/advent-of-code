#!/usr/bin/env python
import fileinput


def compare(left, right) -> str:
    if isinstance(left, int):
        if isinstance(right, int):
            if left < right:
                return '👍'
            if right < left:
                return '👎'
            return '🤷‍♂️'
        elif isinstance(right, list):
            return compare([left], right)
    if isinstance(left, list):
        if isinstance(right, int):
            return compare(left, [right])
        elif isinstance(right, list):
            for i in range(min(len(left), len(right))):
                result = compare(left[i], right[i])
                if result == '👍' or result == '👎':
                    return result
            if len(left) < len(right):
                return '👍'
            if len(right) < len(left):
                return '👎'
            return '🤷‍♂️'


pairs = [[]]
right_order_sum = 0

for line in fileinput.input():
    if line[0] == '\n':
        pairs.append([])
        continue
    pairs[-1].append(eval(line))  # eval ftw

for i, pair in enumerate(pairs):
    if compare(pair[0], pair[1]) == '👍':
        right_order_sum += i + 1

print(f'Sum of indices of correctly ordered pairs: {right_order_sum}')
