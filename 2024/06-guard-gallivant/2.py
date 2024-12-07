#!/usr/bin/env python
import sys
import time

obstacles = set()
new_obstacle = None
visited = set()
SIZE_X = 0
SIZE_Y = 0
guard = None
loops = 0

class Guard:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def tick(self):  # returns false if guard has left or is in a loop
        # print(f'Guard at ({self.x}, {self.y})')
        # check if we've left the area
        if self.x < 0 or self.x >= SIZE_X or self.y < 0 or self.y >= SIZE_Y:
            return False
        if (self.x, self.y, self.direction) in visited:
            global loops
            loops += 1
            print('Found loop with new obstacle', new_obstacle)
            print('Guard at', self.x, self.y)
            return False
        
        visited.add((self.x, self.y, self.direction))
        (new_x, new_y) = (self.x, self.y-1) if self.direction == '^'\
            else (self.x+1, self.y) if self.direction == '>'\
            else (self.x, self.y+1) if self.direction == 'V'\
            else (self.x-1, self.y)
        
        # check for obstacles
        if (new_x, new_y) in obstacles or new_obstacle == (new_x, new_y):
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
    
    def copy(self):
        return Guard(self.x, self.y, self.direction)

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
                # print(f'Guard start:', x, y, c)
                guard = Guard(x, y, c)

print(SIZE_X, SIZE_Y)

# brute forcing out of laziness and curiosity for how long it'll take
start_time = time.time()
for y in range(SIZE_Y):
    for x in range(SIZE_X):
        if (x, y) in obstacles or (x == guard.x and y == guard.y):
            continue
        visited.clear()
        new_obstacle = (x, y)
        # print('New obstacle:', new_obstacle)
        temp_guard = guard.copy()
        while temp_guard.tick():
            pass
end_time = time.time()
elapsed_time = end_time - start_time
        
# while guard.tick():
#     pass

print(f'Found solution in {elapsed_time} seconds')
# print(len(visited))
print(loops)

# 2023 - too high