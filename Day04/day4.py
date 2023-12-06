#!/bin/env python3

import sys
import re

def parse_number_list(number_list: str) -> list[int]:
    regex_results = re.findall('([0-9]+)', number_list)
    return regex_results

def parse_card_number(txt: str) -> int|None:
    result = re.search('[c|C]ard\s+([0-9]+)', txt)
    if result == None:
        return None
    return result.group(1)

def main(argv):
    if len(argv) != 2:
        print("Usage: day4.py inputfile")
        exit(1)

    lines = []
    with open(argv[1], 'r') as f:
        lines = f.readlines()
    
    pile_points = 0
    for line in lines:
        parts = line.split(':')
        card_number = parse_card_number(parts[0])

        numbers_str = parts[1].split('|')
        winning_numbers = parse_number_list(numbers_str[0])
        my_numbers = parse_number_list(numbers_str[1])

        points = 0
        for my_number in my_numbers:
            for winning_number in winning_numbers:
                if my_number == winning_number:
                    if points == 0:
                        points = 1
                    else:
                        points = points * 2
        pile_points = pile_points + points

        print(f'Card {card_number} has {points} points')

    print(f'In total, you have {pile_points} points')

if __name__ == '__main__':
    main(sys.argv)