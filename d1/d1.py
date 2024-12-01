#Advent of code 2024 Day 1 - Historian Hysteria
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd1.txt'

l1, l2 = [], []
with open(file_path, 'r') as f: 
    for line in f: 
        line = line.split()
        l1.append(int(line[0]))
        l2.append(int(line[1]))

l1.sort()
l2.sort()

part_one = 0
part_two = 0
for i in range(len(l1)):
    part_one += abs(l1[i] - l2[i])
    part_two += l2.count(l1[i]) * l1[i]

print(f'Part 1: {part_one}')
print(f'Part 2: {part_two}')