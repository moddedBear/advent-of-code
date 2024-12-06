#!/usr/bin/env python
import sys

grid = []
X_SIZE = None
Y_SIZE = None

def check_x(x, y):
    if x < 0 or x >= X_SIZE or y < 0 or y >= Y_SIZE:
        return False
    if grid[y][x] != 'A':
        return False
    nw = grid[y-1][x-1]
    ne = grid[y-1][x+1]
    sw = grid[y+1][x-1]
    se = grid[y+1][x+1]
    if not ((nw == 'M' and se == 'S') or (nw == 'S' and se == 'M')):
        return False
    if not ((ne == 'M' and sw == 'S') or (ne == 'S' and sw == 'M')):
        return False
    return True

filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        grid.append(line)

X_SIZE = len(grid[0]) - 1
Y_SIZE = len(grid)
result = 0
for y in range(1, Y_SIZE-1):
    for x in range(1, X_SIZE-1):
        if check_x(x, y):
            result += 1

print(result)