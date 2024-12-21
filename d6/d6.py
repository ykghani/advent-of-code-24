#Advent of Code 2024 - Day 6 Guard Gullivant 

from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd6.txt'

with open(file_path, 'r') as f: 
    grid = [list(line.strip()) for line in f]
    
num_rows = len(grid)
num_cols = len(grid[0])

