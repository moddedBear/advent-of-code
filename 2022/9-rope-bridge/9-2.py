#!/usr/bin/env python
import fileinput
import math

rope = [[0, 0] for _ in range(10)]

visited = {(0, 0)}


def updateTail(h, t):
    dx = h[0] - t[0]
    dy = h[1] - t[1]
    distance = math.sqrt((dx**2) + (dy**2))
    if distance < 2:
        return

    if h[0] == t[0]:
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1
    elif h[1] == t[1]:
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1
    else:  # diagonal move
        if h[1] > t[1]:
            t[1] += 1
        else:
            t[1] -= 1
        if h[0] > t[0]:
            t[0] += 1
        else:
            t[0] -= 1


def moveX(x: int):
    step = x // abs(x)
    for _ in range(abs(x)):
        rope[0][0] += step
        for i in range(len(rope) - 1):
            updateTail(rope[i], rope[i + 1])
        visited.add((rope[-1][0], rope[-1][1]))


def moveY(y: int):
    step = y // abs(y)
    for _ in range(abs(y)):
        rope[0][1] += step
        for i in range(len(rope) - 1):
            updateTail(rope[i], rope[i + 1])
        visited.add((rope[-1][0], rope[-1][1]))


for line in fileinput.input():
    line_list = line.split(' ')
    direction = line_list[0]
    distance = int(line_list[1])
    if direction == 'L' or direction == 'D':
        distance = distance * -1
    if direction == 'U' or direction == 'D':
        moveY(distance)
    else:
        moveX(distance)

# for v in sorted(list(visited)):
#     print(v)
print(len(visited))
