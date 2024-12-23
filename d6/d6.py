#Advent of Code 2024 - Day 6 Guard Gullivant 

from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd6.txt'

with open(file_path, 'r') as f: 
    grid = [list(line.strip()) for line in f]

# grid = ['....#.....',
#         '.........#',
#         '..........',
#         '..#.......',
#         '.......#..',
#         '..........',
#         '.#..^.....',
#         '........#.',
#         '#.........',
#         '......#...']

# grid = [list(row) for row in grid]
    
row_dim = len(grid)
col_dim = len(grid[0])

dirs = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

start_i, start_j = next((i, j) for i, row in enumerate(grid)
                        for j, val in enumerate(row) if val == '^')

def move(grid, cur_pos, obstacle_count):
    dir = dirs[obstacle_count % 4]
    i, j = cur_pos[0], cur_pos[1]
    while True:
        grid[i][j] = 'X'
        i += dir[0]
        j += dir[1]
        
        if not (0 <= i < row_dim and 0 <= j < col_dim):
            return (i - dir[0], j - dir[1]), False 
        
        if grid[i][j] == '#':
            obstacle_count += 1
            return (i - dir[0], j - dir[1]), True
        



guard_present = True
cur = (start_i, start_j)
obstacles_encountered = 0
while guard_present:
    
    cur, guard_present = move(grid, cur, obstacles_encountered)
    obstacles_encountered += 1
    
print(f'Part one: {sum(row.count('X') for row in grid)}')
