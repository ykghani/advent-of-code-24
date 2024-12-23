#Advent of Code 2024: Hoof it

from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd10.txt'

grid = []
with open(file_path, 'r') as f:
    for line in f: 
        grid.append([int(n) for n in line.strip()])

num_rows, num_cols = len(grid), len(grid[0])

def get_neighbors(grid, cur) -> list: 
    row_dim, col_dim = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    neighbors = []
    for dir in directions:
        x = cur[0] + dir[0]
        y = cur[1] + dir[1]
        if 0 <= x < row_dim and 0 <= y < col_dim:
            neighbors.append((x, y))
    
    return neighbors

def score_trail(grid, trailhead, skip_visited) -> int:
    score = 0
    visited = set()
    queue = [trailhead]
    
    while queue:
        cur = queue.pop()
        
        if skip_visited:
            if cur in visited: 
                continue
        
        visited.add(cur)
        
        if grid[cur[0]][cur[1]] == 9:
            score += 1
            continue
        
        queue.extend(
            n for n in get_neighbors(grid, cur) if grid[n[0]][n[1]] == grid[cur[0]][cur[1]] + 1
        )
    return score

part_one = False
trail_sum = 0
for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] == 0:
            trail_sum += score_trail(grid, (i, j), part_one)

print(f"Answer: {trail_sum}")        