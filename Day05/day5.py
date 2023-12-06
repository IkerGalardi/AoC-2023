#!/bin/env python3

import sys
import re

class TranslationRange:
    def __init__(self, destination_start: int, source_start: int, num: int):
        self.source_start = source_start
        self.destination_start = destination_start
        self.num = num

SEEDS: list[int] = []
TRANSLATION_MAP = {
    'seed-to-soil': [],
    'soil-to-fertilizer': [],
    'fertilizer-to-water': [],
    'water-to-light': [],
    'light-to-temperature': [],
    'temperature-to-humidity': [],
    'humidity-to-location': []
}

def parse_map_file(lines: list[str]):
    map_type: str = ''
    for line in lines:
        if line.startswith('seeds:'):
            seeds = re.findall('[0-9]+', line.split(':')[1])
            for seed in seeds:
                SEEDS.append(int(seed))
        elif line.startswith('seed-to-soil'):
            map_type = 'seed-to-soil'
        elif line.startswith('soil-to-fertilizer'):
            map_type = 'soil-to-fertilizer'
        elif line.startswith('fertilizer-to-water'):
            map_type = 'fertilizer-to-water'
        elif line.startswith('water-to-light'):
            map_type = 'water-to-light'
        elif line.startswith('light-to-temperature'):
            map_type = 'light-to-temperature'
        elif line.startswith('temperature-to-humidity'):
            map_type = 'temperature-to-humidity'
        elif line.startswith('humidity-to-location'):
            map_type = 'humidity-to-location'
        else:
            numbers = re.findall('[0-9]+', line)
            if len(numbers) == 3:
                TRANSLATION_MAP[map_type].append(TranslationRange(int(numbers[0]), int(numbers[1]), int(numbers[2])))

def seed_to_location(seed: int) -> int:
    def translate_unique_stage(value: int, stage: str) -> int:
        print(f'Translation stage {stage}')
        tmp = value
        translation_map = TRANSLATION_MAP[stage]
        for translation_range in translation_map:
            range_start = translation_range.source_start
            range_end = range_start + translation_range.num
            if range_start <= tmp < range_end:
                print(f'Value {value} IS in the range ({range_start}, {range_end})')
                offset = tmp - range_start
                tmp = translation_range.destination_start + offset
                print(f'Value {value} gets mapped into {tmp} = {translation_range.destination_start} + {offset}')
                return tmp
            else:
                print(f'Value {value} NOT in the range ({range_start}, {range_end})')
        print(f'Value {value} gets mapped into {tmp}')
        return tmp

    soil = translate_unique_stage(seed,'seed-to-soil')
    fertilizer = translate_unique_stage(soil,'soil-to-fertilizer')
    water = translate_unique_stage(fertilizer, 'fertilizer-to-water')
    light = translate_unique_stage(water, 'water-to-light')
    temperature = translate_unique_stage(light, 'light-to-temperature')
    humidity = translate_unique_stage(temperature, 'temperature-to-humidity')
    location = translate_unique_stage(humidity,  'humidity-to-location')
    print(f'Seed {seed} -> {soil} -> {fertilizer} -> {water} -> {water} -> {light} -> {temperature} -> {humidity} -> {location}')
    return location


def main(argv: list[str]):
    lines = []
    with open(argv[1], 'r') as f:
        lines = f.readlines()

    parse_map_file(lines)
    seed_locations = []
    for seed in SEEDS:
        location = seed_to_location(seed)
        seed_locations.append(location)

    print(f'Lowest location number is {min(seed_locations)}')

if __name__ == '__main__':
    main(sys.argv)