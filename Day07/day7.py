#!/bin/env python3

import sys

FIVE_OF_A_KIND =  6
FOUR_OF_A_KIND =  5
FULL_HOUSE =      4
THREE_OF_A_KIND = 3
TWO_PAIR =        2
ONE_PAIR =        1
HIGH_CARD =       0
def cards_type(cards: str) -> int:
    card_occurrences = {}
    for card in cards:
        if card in card_occurrences.keys():
            card_occurrences[card] += 1
        else:
            card_occurrences[card] = 1

    if len(card_occurrences) == 5:
        return HIGH_CARD
    elif len(card_occurrences) == 2:
        values = list(card_occurrences.values())
        values.sort()
        if values == [2, 3]:
            return FULL_HOUSE
        elif values == [1, 4]:
            return FOUR_OF_A_KIND
        else:
            print('ELSE CASE IN TWO CARD OCCURRENCES')
    elif len(card_occurrences) == 1:
        return FIVE_OF_A_KIND
    else:
        values = list(card_occurrences.values())
        values.sort()
        if values == [1, 1, 3]:
            return THREE_OF_A_KIND
        elif values == [1, 2, 2]:
            return TWO_PAIR
        else:
            return ONE_PAIR

def card_to_power(card) -> int:
    if   card == 'A':
        return 12
    elif card == 'K':
        return 11
    elif card == 'Q':
        return 10
    elif card == 'J':
        return 9
    elif card == 'T':
        return 8
    elif card == '9':
        return 7
    elif card == '8':
        return 6
    elif card == '7':
        return 5
    elif card == '6':
        return 4
    elif card == '5':
        return 3
    elif card == '4':
        return 2
    elif card == '3':
        return 1
    elif card == '2':
        return 0
    print("SOMETHING IS RONG")
    return -1

class Hand:
    def __init__(self, hand: str, bid: int):
        self.cards = hand
        self.bid = bid
    
    def better_than(self, other) -> bool:
        type_left = cards_type(self.cards)
        type_right = cards_type(other.cards)
        if type_left > type_right:
            return True
        elif type_left < type_right:
            return False
        else:
            for left_card, right_card in zip(self.cards, other.cards):
                if card_to_power(left_card) > card_to_power(right_card):
                    return True
                elif card_to_power(left_card) < card_to_power(right_card):
                    return False
        print('CARDS_EQUAL')
        return False

def insertion_sort(array: list[Hand]) -> list[Hand]:
    result = array.copy()
    for i in range(1, len(result)):
        hand = result[i]
        j = i - 1
        while j >= 0 and result[j].better_than(hand):
            result[j + 1] = result[j]
            j = j - 1
        result[j + 1] = hand
    return result

def main(argv):
    lines = []
    with open(argv[1], 'r') as f:
        lines = f.readlines()

    hands: list[Hand] = []
    for line in lines:
        parts = line.split(' ')
        hands.append(Hand(parts[0], int(parts[1])))

    hands = insertion_sort(hands)
    total_winnings = 0
    i = 1
    for hand in hands:
        print(f'Cards "{hand.cards}" bid {hand.bid}. Winnings are {hand.bid} * {i} = {hand.bid * i}')
        total_winnings += hand.bid * i
        i += 1
    
    print(f'Total winnings are {total_winnings}')


if __name__ == '__main__':
    main(sys.argv)