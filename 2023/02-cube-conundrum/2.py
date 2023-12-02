#!/usr/bin/env python
import sys
import re

# we need to find the sum of the power of each game
# a game's power is found by multiplying the minimum number of red, green, and blue cubes it could have been played with

filename = sys.argv[1]
result = 0
with open(filename) as f:
    for line in f:
        # first split the line into the game info and results
        # plus a check for blank lines because I'm too lazy to remove the blank line at the end of my input file
        game_split = line.split(':')
        if not len(game_split) == 2:
            continue
        game_text, results_text = game_split

        # get the game number using regex
        game_match = re.search(r'\d+', game_text)
        game_num = int(game_match[0]) if game_match else exit(1)

        # split the result sets so we can go through them individually
        result_sets = results_text.split(';')
        red_min = blue_min = green_min = 0
        for result_set in result_sets:
            # find the number of each cube using regex
            red_match = re.search(r'(\d+) red', result_set)
            blue_match = re.search(r'(\d+) blue', result_set)
            green_match = re.search(r'(\d+) green', result_set)
            red = int(red_match.group(1)) if red_match else 0
            blue = int(blue_match.group(1)) if blue_match else 0
            green = int(green_match.group(1)) if green_match else 0

            red_min = max(red_min, red)
            blue_min = max(blue_min, blue)
            green_min = max(green_min, green)
        power = red_min * blue_min * green_min
        result += power

print(result)
