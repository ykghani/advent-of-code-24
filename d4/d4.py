#--- Day 4: Ceres Search ---
from pathlib import Path 

script_dir = Path(__file__).parent
file_path = script_dir / 'd4.txt'

match = 'XMAS'
directions = [(0, 1), (1, 1), (1, 0), (1, -1), 
              (0, -1), (-1, -1), (-1, 0), (-1, 1)]

diagonals = [[(-1, -1), (1, 1)],
             [(-1, 1), (1, -1)]]

def is_valid(x, y):
    return 0 <= x < x_lim and 0 <= y < y_lim

def check_direction(start_x, start_y, dx, dy):
    # Check if we can make a complete "XMAS" from this position and direction
    target = "XMAS"
    positions_found = []
    
    for i, char in enumerate(target):
        x = start_x + i * dx
        y = start_y + i * dy
        
        if not is_valid(x, y) or grid[x][y] != char:
            return False, []
        
        positions_found.append((x, y))
        
    return True, positions_found

grid = []
with open(file_path, 'r') as f: 
    for line in f:
        grid.append(list(line.strip()))

part_one = part_two = 0
positions = []
x_lim, y_lim = len(grid[0]), len(grid)
for x in range(x_lim):
    for y in range(y_lim):
        if grid[x][y] == 'X':
            for dx, dy in directions: 
                found, pos = check_direction(x, y, dx, dy)
                if found: 
                    part_one += 1

print(f"Part one: {part_one}")

def is_xmas(x, y, grid= grid) -> bool:
    '''Returns true if char is center of X-MAS shape and False otherwise'''
    comparator = {'M', 'S'}
    if grid[y][x] != "A":
        return False
    else:
        return {grid[y + 1][x - 1], grid[y - 1][x + 1]} == comparator and {grid[y - 1][x - 1], grid[y + 1][x + 1]} == comparator

#Part Two#
for y in range(1, y_lim - 1):
    for x in range(1, x_lim - 1): #Stay within bounding box to prevent index out of range issues
        if is_xmas(y, x, grid):
            part_two += 1

print(f"Part two : {part_two}")
