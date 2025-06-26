'''Advent of Code 2024 Day 14: Restroom Redoubt'''

from pathlib import Path
from collections import namedtuple
from functools import reduce
import matplotlib.pyplot as plt 

script_dir = Path(__file__).parent
file_path = script_dir / 'd14.txt'

Robot = namedtuple('Robot', ['pos', 'vel'])

NUM_ROWS = 103
NUM_COLS = 101
SECONDS = 100

def parse_line(line: str):
    pos_part, vel_part = line.strip().split()
        
    pos = [int(x) for x in pos_part[2:].split(',')]
    vel = [int(x) for x in vel_part[2:].split(',')]
    
    return Robot(pos, vel)

def define_quadrants(row_dim, col_dim) -> dict:
    '''Return quadrant dimensions in format <column limits , row limits>'''
    
    col_split = (col_dim - 1) // 2 #50 
    row_split = (row_dim - 1) // 2  
    
    return {'TL': [range(0, col_split), range(0, row_split)],
            'TR': [range(col_split + 1, col_dim), range(0, row_split)],
            'BL': [range(0, col_split), range(row_split + 1, row_dim)],
            'BR': [range(col_split + 1, col_dim), range(row_split + 1, row_dim)]
            }

def find_quadrant(pos, quad_dict):
    col_val, row_val = pos[0], pos[1]
    
    for quad in quad_dict.keys():
        quad_limits = quad_dict[quad]
        if col_val in quad_limits[0] and row_val in quad_limits[1]:
            return quad
    
    return None

def move(robot: Robot):
    cur_x, cur_y = robot.pos[0], robot.pos[1]
    
    if cur_x + robot.vel[0] >= NUM_COLS:
        new_x = cur_x + robot.vel[0] - NUM_COLS
    elif cur_x + robot.vel[0] < 0: 
        new_x = NUM_COLS + cur_x + robot.vel[0]
    else: 
        new_x = cur_x + robot.vel[0]
    
    if cur_y + robot.vel[1] >= NUM_ROWS:
        new_y = cur_y + robot.vel[1] - NUM_ROWS
    elif cur_y + robot.vel[1] < 0: 
        new_y = NUM_ROWS + cur_y + robot.vel[1]
    else:
        new_y = cur_y + robot.vel[1]
    
    return Robot([new_x, new_y], robot.vel)
    

robots = []
quad_counts = {'TL': 0, 'TR': 0, 'BL': 0, 'BR': 0}
quad_limits = define_quadrants(NUM_ROWS, NUM_COLS)
with open(file_path, 'r') as f:
    for line in f: 
        robot = (parse_line(line))
        robots.append(robot)
        for _ in range(SECONDS):
            robot = move(robot)
        
        quadrant = find_quadrant(robot.pos, quad_limits)
        if quadrant:
            quad_counts[quadrant] += 1

print(f"Part 1: {reduce(lambda x, y: x * y, quad_counts.values())}")

#Part two: 
def plot_robots(robots, second_val):

    x_coords = [robot.pos[0] for robot in robots]
    y_coords = [robot.pos[1] for robot in robots]
    
    plt.figure(figsize=(10, 10))
    plt.scatter(x_coords, y_coords, c='blue', marker='o', s=105)
    
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Robot Positions')
    
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.axis('equal')

    output_file = f"SECOND_{second_val + 1}.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()


for s in range(SECONDS + 900):
    updated_robots = [move(robot) for robot in robots]
    plot_robots(updated_robots, s)
    robots = updated_robots

