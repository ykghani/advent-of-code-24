#Advent of Code 2024 - Day 5: Print Queue

from pathlib import Path
from collections import defaultdict

script_dir = Path(__file__).parent
file_path = script_dir / 'd5_test.txt'

ordering_rules = defaultdict(list)
print_seqs = []

with open(file_path, 'r') as f: 
    for line in f: 
        line = line.strip()
        if '|' in line: 
            precedent, page = line.split('|')
            ordering_rules[int(page)].append(int(precedent))
        elif ',' in line.strip():
            print_seqs.append([int(i) for i in line.split(',')])
            

part_one = 0 
part_two = 0

for seq in print_seqs:
    ordered = True
    updated_seq = []
    skip = False
    for idx, num in enumerate(seq):
        if idx == 0:
            continue
        precedents = seq[:idx]
        for prec in precedents:
            if prec not in ordering_rules[num]:
                ordered = False
                updated_seq.append(num)
                updated_seq.append(prec)
                skip = True
                
        if skip:
            skip = False
        else: 
            updated_seq.append(num)
    
    if ordered:
        part_one += seq[(len(seq) - 1) // 2]
    else:
        part_two += updated_seq[(len(updated_seq) - 1) // 2]

print(part_one)
print(f"Part two answer: {part_two}")        