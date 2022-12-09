#!/usr/bin/env python
import fileinput

head = [0, 0]  # x, y
tail = [0, 0]

visited = {(0, 0)}


def updateTail():
    if head[0] - tail[0] > 1:  # head too far to right
        tail[0] += 1
        tail[1] = head[1]
        visited.add((tail[0], tail[1]))
    elif tail[0] - head[0] > 1:  # head too far to left
        tail[0] -= 1
        tail[1] = head[1]
        visited.add((tail[0], tail[1]))
    if head[1] - tail[1] > 1:  # head too far above
        tail[1] += 1
        tail[0] = head[0]
        visited.add((tail[0], tail[1]))
    elif tail[1] - head[1] > 1:  # head too far below
        tail[1] -= 1
        tail[0] = head[0]
        visited.add((tail[0], tail[1]))


def moveX(x: int):
    step = x // abs(x)
    for _ in range(abs(x)):
        head[0] += step
        updateTail()


def moveY(y: int):
    step = y // abs(y)
    for _ in range(abs(y)):
        head[1] += step
        updateTail()


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

print(len(visited))
