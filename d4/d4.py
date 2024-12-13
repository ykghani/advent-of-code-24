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

def check_mas(x, y, dx, dy):
    """Check for 'MAS' or 'SAM' in given direction starting at (x,y)"""
    if not is_valid(x, y) or not is_valid(x + 2 * dx, y + 2 * dy):
        return False, [], ""
    
    # Get the three characters in this direction
    chars = [grid[x + i * dx][y + i * dy] for i in range(3)]
    sequence = ''.join(chars)
    positions = [(x + i * dx, y + i * dy) for i in range(3)]
    
    # Check if it's 'MAS' forward or 'SAM' backward
    if sequence == 'MAS':
        return True, positions, 'MAS'
    elif sequence == 'SAM':
        return True, positions, 'SAM'
    return False, [], ""

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
        elif grid[x][y] == 'A':
            for (dx1, dy1), (dx2, dy2) in diagonals:
                found1, pos1, seq1 = check_mas(x + dx1, y + dy1, dx1, dy1)
                if not found1:
                    continue
                    
                found2, pos2, seq2 = check_mas(x + dx2, y + dy2, dx2, dy2)
                if not found2:
                    continue
                
                # Found valid X-MAS pattern
                part_two += 1
                # Include center position and both diagonals
                pattern_positions = [(x, y)] + pos1 + pos2
                positions.append(pattern_positions)
print(f"Part one: {part_one}")
print(f"Part two : {part_two}")
