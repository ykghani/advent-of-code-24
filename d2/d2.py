#Advent of code 2024 Day 2 - Red-Nosed Reports
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd2.txt'

SKIP_MIN = 1
SKIP_MAX = 3

def check_safety(num_list: list) -> bool:
    return all(
        (int(a) < int(b) and abs(a - b) >= SKIP_MIN and abs(a - b) <= SKIP_MAX)
        for a, b in zip(num_list, num_list[1: ])
    ) or all(
        (int(a) > int(b) and abs(a - b) >= SKIP_MIN and abs(a - b) <= SKIP_MAX)
        for a, b in zip(num_list, num_list[1: ])
    )    

part_one, part_two = 0, 0
with open(file_path, 'r') as f: 
    for line in f: 
        report = [int(i) for i in line.strip().split()]
        part_one += 1 if check_safety(report) else 0
        part_two += any([check_safety(report[:i] + report[i + 1:]) for i in range(len(report))])

print(f"Part 1: {part_one}")
print(f"Part 2: {part_two}")