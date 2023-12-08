#!/bin/env python3

import day7

def test_cards_type(cards: str, expected: int):
    result = day7.cards_type(cards)
    if result == expected:
        print(f'Cards "{cards}": PASS')
    else:
        print(f'Cards "{cards}": FAIL. Expecting {expected}, got {result}')

def test_card_better_than(left_cards: str, right_cards: str, expected: bool):
    left = day7.Hand(left_cards, 0)
    right = day7.Hand(right_cards, 0)
    result = left.better_than(right)
    if result == expected:
        print(f'"{left_cards}" > "{right_cards} == {expected}": PASS')
    else:
        print(f'"{left_cards}" > "{right_cards} == {expected}": FAIL.')

test_cards_type("AAAAA", day7.FIVE_OF_A_KIND)
test_cards_type("AA8AA", day7.FOUR_OF_A_KIND)
test_cards_type("23332", day7.FULL_HOUSE)
test_cards_type("TTT98", day7.THREE_OF_A_KIND)
test_cards_type("23432", day7.TWO_PAIR)
test_cards_type("A23A4", day7.ONE_PAIR)
test_cards_type("23456", day7.HIGH_CARD)
test_cards_type("32T3K", day7.ONE_PAIR)
test_cards_type("KK677", day7.TWO_PAIR)
test_cards_type("KTJJT", day7.TWO_PAIR)
test_cards_type("T55J5", day7.THREE_OF_A_KIND)
test_cards_type("33332", day7.FOUR_OF_A_KIND)
test_cards_type("2AAAA", day7.FOUR_OF_A_KIND)
test_cards_type("77888", day7.FULL_HOUSE)
test_cards_type("77788", day7.FULL_HOUSE)

test_card_better_than("KTJJT", "KK677", False)
test_card_better_than("33332", "2AAAA", True)
test_card_better_than("77888", "77788", True)