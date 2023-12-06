#!/bin/env python3

import sys
import re

def parse_input(lines: list[str]) -> (list[int], list[int]):
    times_str = re.findall('[0-9]+', lines[0])
    distances_str = re.findall('[0-9]+', lines[1])

    times = []
    distances = []
    for time_str, distance_str in zip(times_str, distances_str):
        times.append(int(time_str))
        distances.append(int(distance_str))

    return (times, distances)

def calculate_distance(ms_pressed: int, max_time: int) -> int:
    time_left = max_time - ms_pressed
    return time_left * ms_pressed

def main(argv):
    lines = []
    with open(argv[1], 'r') as f:
        lines = f.readlines()

    times, distances = parse_input(lines)

    num_winnable_games = []
    for time, record_distance in zip(times, distances):
        time_num_winnable_games = 0
        for i in range(0, time):
            distance = calculate_distance(i, time)
            if distance > record_distance:
                time_num_winnable_games = time_num_winnable_games + 1
        num_winnable_games.append(time_num_winnable_games)
        
    margin_of_error = 1
    for num in num_winnable_games:
        margin_of_error = margin_of_error * num
    
    print(f'Margin of error is {margin_of_error}')

if __name__ == '__main__':
    main(sys.argv)