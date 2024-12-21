#Advent of Code 2024 - Day 9 Disk Fragmenter

from pathlib import Path
from collections import defaultdict

script_dir = Path(__file__).parent
file_path = script_dir / 'd9.txt'

with open(file_path) as f: 
    INPUT = f.read()

# INPUT = '2333133121414131402'

expansion = []
idx = 0
for i, char in enumerate(INPUT):
    length = int(char)
    if i % 2 == 0: 
        expansion.extend([str(idx)] * length)
        idx += 1
    else: 
        expansion.extend(list('.' * int(char)))

part_two = expansion.copy() 

#Perform space swapping for part 1
i = 0
last_idx = len(expansion) - 1
while i < last_idx: 
    if expansion[i] == '.':
        while last_idx > i and expansion[last_idx] == '.':
            last_idx -= 1
        
        if i < last_idx:  
            expansion[i], expansion[last_idx] = expansion[last_idx], expansion[i]
            last_idx -= 1
    
    i += 1

checksum = 0
for idx, char in enumerate(expansion):
    if char != '.':
        checksum += idx * int(char)

print(f'Part one: {checksum}')

def find_free_space(blocks, start_pos, length_needed):
    """Find the leftmost free space that can fit the file."""
    i = 0
    current_length = 0
    start_of_space = None
    
    while i < start_pos:
        if blocks[i] == '.':
            if start_of_space is None:
                start_of_space = i
            current_length += 1
            if current_length >= length_needed:
                return start_of_space
        else:
            start_of_space = None
            current_length = 0
        i += 1
    
    return None

def move_file(blocks, file_positions, new_start):
    file_id = blocks[file_positions[0]]
    file_length = len(file_positions)
    
    
    for pos in file_positions:
        blocks[pos] = '.'
        
    # Place file in new position
    for i in range(file_length):
        blocks[new_start + i] = file_id

#Create list of spaces and files with lengths
files = defaultdict(list)
for idx, char in enumerate(part_two):
    if char != '.':
        files[int(char)].append(idx) 

# Process files in reverse order
for file_id in sorted(files.keys(), reverse=True):
    positions = files[file_id]
    file_length = len(positions)  
    min_pos = min(positions)
    
    new_pos = find_free_space(part_two, min_pos, file_length)
    
    if new_pos is not None and new_pos < min_pos:
        move_file(part_two, positions, new_pos)


checksum = 0
for idx, char in enumerate(part_two):  
    if char != '.':
        checksum += idx * int(char)
        
print(f"Part two: {checksum}")