#!/bin/env python3

import sys
import re

def parse_reveal(reveal):
    num_red = 0
    num_green = 0
    num_blue = 0

    reveal = reveal.split(',')
    for single_reveal in reveal:
        single_reveal = single_reveal.strip()
        result = re.search("([0-9]+)\sred", single_reveal)
        if result != None:
            num_red = int(result.group(1))
        result = re.search("([0-9]+)\sgreen", single_reveal)
        if result != None:
            num_green = int(result.group(1))
        result = re.search("([0-9]+)\sblue", single_reveal)
        if result != None:
            num_blue = int(result.group(1))

    return (num_red, num_green, num_blue)

def game_possible(game_str):
    MAX_RED_CUBES = 12
    MAX_GREEN_CUBES = 13
    MAX_BLUE_CUBES = 14

    possible = True
    reveals = game_str.split(';')
    for reveal in reveals:
        red, green, blue = parse_reveal(reveal)
        if red > MAX_RED_CUBES:
            possible = False
            break
        if green > MAX_GREEN_CUBES:
            possible = False
            break
        if blue > MAX_BLUE_CUBES:
            possible = False
            break

    return possible

def main():
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    # Loop through each game
    i = 1
    sum = 0
    for line in lines:
        line = line[8:-1]


        if game_possible(line):
            sum = sum + i

        i = i + 1

    print(f"Sum of possible IDs is {sum}")

if __name__ == '__main__':
    main()