#!/bin/env python3

import day2

def test_parse_reveal(single_reveal, expected):
    result = day2.parse_reveal(single_reveal)
    if result ==  expected:
        print(f"{single_reveal} -- PASS")
    else:
        red, green, blue = result
        print(f"{single_reveal} -- FAIL. Got red={red}, green={green}, blue={blue}")

def test_game_possible(game, expected):
    result = day2.game_possible(game)
    if result == expected:
        print(f'{game}: PASS')
    else:
        print(f'{game}: FAIL. Expected {expected}, got {result}')

print("-- test_parse_reveal --")
test_parse_reveal("12 red, 14 green, 1 blue", (12, 14, 1))
test_parse_reveal("12 red, 1 blue", (12, 0, 1))
test_parse_reveal("8 green, 6 blue, 20 red", (20, 8, 6))
print("-- END --")
print("")

print("-- test_game_possible --")
test_game_possible('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', True)
test_game_possible('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', True)
test_game_possible('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', False)
test_game_possible('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', False)
test_game_possible('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', True)
print("-- END --")
