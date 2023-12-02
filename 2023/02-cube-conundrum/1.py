#!/usr/bin/env python
import sys
import re

# we need to add up the game IDs of the games that would have been
# possible with this many cubes
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

filename = sys.argv[1]
result = 0
with open(filename) as f:
    for line in f:
        game_split = line.split(':')
        if not len(game_split) == 2:
            continue
        game_text, results_text = game_split
        game_match = re.search(r'\d+', game_text)
        game_num = int(game_match[0]) if game_match else exit(1)

        result_sets = results_text.split(';')
        is_possible = True
        for result_set in result_sets:
            red_match = re.search(r'(\d+) red', result_set)
            blue_match = re.search(r'(\d+) blue', result_set)
            green_match = re.search(r'(\d+) green', result_set)
            red = int(red_match.group(1)) if red_match else 0
            blue = int(blue_match.group(1)) if blue_match else 0
            green = int(green_match.group(1)) if green_match else 0
            if red > RED_MAX or blue > BLUE_MAX or green > GREEN_MAX:
                is_possible = False
                break
        if is_possible:
            result += game_num

print(result)
