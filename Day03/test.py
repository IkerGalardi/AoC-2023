#!/bin/env python3

import day3

def test_process_line(line, up, down, expected):
    result = day3.process_line(line, up, down)
    if result == expected:
        print(f'Line {line}. PASS')
    else:
        print(f'Line {line}. FAIL. Expected {expected}, got {result}')

test_process_line('467..114..', None,         '...*......', [467])
test_process_line('..35..633.', '...*......', '......#...', [35, 633])
test_process_line('617*......', None, None, [617])