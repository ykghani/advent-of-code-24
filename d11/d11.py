'''Advent of Code 2024 Day 11 - Plutonian Pebbles'''

from pathlib import Path
from collections import defaultdict

script_dir = Path(__file__).parent
file_path = script_dir / 'd11.txt'

with open(file_path, 'r') as f:
    stones = [int(n) for n in f.readline().split()]

part_two = {n: 1 for n in stones}


def blink(stones): 
    output = []
    
    for stone in stones: 
        if stone == 0:
            output.append(1)
        elif len(str(stone)) % 2 == 0: 
            tmp = str(stone)
            split_ind = len(tmp) // 2
            a, b = int(tmp[:split_ind]), int(tmp[split_ind: ])
            output.append(a)
            output.append(b)
        else: 
            output.append(stone * 2024)
    
    return output

for i in range(25):
    stones = blink(stones)

print(f"Part one: {len(stones)}")

#Part 2 
for _ in range(75):
    new_stones = defaultdict(int)
    for stone, val in part_two.items():
        for new_stone in blink([stone]):
            new_stones[new_stone] += val
    
    part_two = new_stones

print(f"Part two: {sum(part_two.values())}")