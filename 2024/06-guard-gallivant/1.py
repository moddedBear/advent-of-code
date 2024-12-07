#!/usr/bin/env python
import sys

obstacles = set()
visited = set()
SIZE_X = 0
SIZE_Y = 0
guard = None

class Guard:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def tick(self):  # returns false if guard has left
        # print(f'Guard at ({self.x}, {self.y})')
        visited.add((self.x, self.y))
        (new_x, new_y) = (self.x, self.y-1) if self.direction == '^'\
            else (self.x+1, self.y) if self.direction == '>'\
            else (self.x, self.y+1) if self.direction == 'V'\
            else (self.x-1, self.y)
        # check if we've left the area
        if new_x < 0 or new_x >= SIZE_X or new_y < 0 or new_y >= SIZE_Y:
            return False
        # check for obstacles
        if (new_x, new_y) in obstacles:
            # turn to the right
            self.direction = '^' if self.direction == '<'\
                else '>' if self.direction == '^'\
                else 'V' if self.direction == '>'\
                else '<'
        else:
            # step forward
            self.x = new_x
            self.y = new_y
        return True

filename = sys.argv[1]
with open(filename, 'r') as f:
    for (y, line) in enumerate(f):
        SIZE_Y += 1
        if SIZE_X == 0:
            SIZE_X = len(line) - 1
        for (x, c) in enumerate(line):
            if c == '#':
                obstacles.add((x, y))
            elif c in ['^', '>', 'V', '<']:
                print(f'Created guard:', x, y, c)
                guard = Guard(x, y, c)

# guard should start at (4, 6)
while guard.tick():
    pass

print(len(visited))