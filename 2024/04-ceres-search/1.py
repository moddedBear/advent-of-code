#!/usr/bin/env python
import sys

grid = []
SEARCH_PHRASE = 'XMAS'
X_SIZE = None
Y_SIZE = None

def in_bounds(x, y):
    return x >= 0 and x < X_SIZE and y >= 0 and y < Y_SIZE

def search_up_left(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_up_left(x-1, y-1, i+1)
    return False

def search_up(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_up(x, y-1, i+1)
    return False

def search_up_right(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_up_right(x+1, y-1, i+1)
    return False

def search_left(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_left(x-1, y, i+1)
    return False

def search_right(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_right(x+1, y, i+1)
    return False

def search_down_left(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_down_left(x-1, y+1, i+1)
    return False

def search_down(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_down(x, y+1, i+1)
    return False

def search_down_right(x, y, i):
    if not in_bounds(x, y): return False
    letter = SEARCH_PHRASE[i]
    if grid[y][x] == letter:
        if i == len(SEARCH_PHRASE) - 1:
            return True
        return search_down_right(x+1, y+1, i+1)
    return False

def search(x, y, i):
    if x < 0 or x >= X_SIZE or y < 0 or y >= Y_SIZE:
        return False
    letter = SEARCH_PHRASE[i]
    result = 0
    if grid[y][x] == letter:
        # up left
        if search_up_left(x-1, y-1, i+1): result += 1
        # up
        if search_up(x, y-1, i+1): result += 1
        # up right
        if search_up_right(x+1, y-1, i+1): result += 1
        # left
        if search_left(x-1, y, i+1): result += 1
        # right
        if search_right(x+1, y, i+1): result += 1
        # down left
        if search_down_left(x-1, y+1, i+1): result += 1
        # down
        if search_down(x, y+1, i+1): result += 1
        # down right
        if search_down_right(x+1, y+1, i+1): result += 1
    return result

filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        grid.append(line)

X_SIZE = len(grid[0]) - 1
Y_SIZE = len(grid)
result = 0
for y in range(Y_SIZE):
    for x in range(X_SIZE):
        result += search(x, y, 0)

print(result)