#!/bin/env python3

import sys
import string

def has_symbol(text):
    for c in text:
        if c == '.':
            continue
        elif c in string.punctuation:
            return True
    return False

def process_line(line: str, up: str, down: str):
    numbers = []
    length = len(line) - 1
    num_start = None
    found = False
    for idx, c in enumerate(line):
        left = max(0, idx - 1)
        right = min(length, idx + 2) # +2 bc is not inclusive

        if c.isdigit() == True:
            if num_start == None:
                num_start = idx

            if not found:
                if has_symbol(line[left:right]):
                    found = True
                elif up != None and has_symbol(up[left:right]):
                    found = True
                elif down != None and has_symbol(down[left:right]):
                    found = True
        else:
            if found:
                num = int(line[num_start:idx])
                numbers.append(num)
                found = False
            
            num_start = None

    if found:
        num = int(line[num_start:idx+1])
        numbers.append(num)
        found = False

    return numbers
            
def main(argv):
    if len(argv) != 2:
        print("Usage: ./day3.py filename")
        exit(1)

    lines = []
    with open(argv[1]) as f:
        lines = f.readlines()

    sum = 0
    for y, line in enumerate(lines):
        line = line[:-1]
        up = None
        if y != 0:
            up = lines[y-1][:-1]
        if y == len(lines) - 1:
            down = None
        else:
            down = lines[y+1][:-1]

        numbers = process_line(line, up, down)
        print(numbers)
        for num in numbers:
            sum = sum + num
    print(f'Sum of part numbers is {sum}')       
            

if __name__ == '__main__':
    main(sys.argv)