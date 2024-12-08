#Advent of Code 2024 - Day 3: Mull it Over
from pathlib import Path
import re

script_dir = Path(__file__).parent
file_path = script_dir / 'd3.txt'

match_pattern = r'mul\(\d{1,3},\d{1,3}\)'

with open(file_path, 'r') as f: 
    text = f.read()
    matches = re.findall(match_pattern, text)

part_one = 0
for match in matches:
    numbers = re.findall(r'\d+', match)
    part_one += int(numbers[0]) * int(numbers[1])
print(f'Part one: {part_one}')  

is_active = True
part_two = 0
chunks = re.split(r'(do\(\))|(don\'t\(\))', text)
for chunk in chunks: 
    if chunk is None:
        continue
    if chunk == 'do()':
        is_active = True
    elif chunk == "don't()":
        is_active = False
    
    if is_active:
        matches = re.findall(match_pattern, chunk)
        for match in matches: 
            numbers = re.findall(r'\d+', match)
            part_two += int(numbers[0]) * int(numbers[1])

print(f"Part two: {part_two}")