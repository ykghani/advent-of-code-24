#Advent of Code 2024 - Day 5: Print Queue

from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd5.txt'

ordering_rules = []
print_seqs = []

with open(file_path, 'r') as f: 
    for line in f: 
        line = line.strip()
        if '|' in line: 
            ordering_rules.append(map(int, line.split('|')))
        elif ',' in line.strip():
            print_seqs.append(list(map(int, line.split(','))))

for seq in print_seqs:
    pass 