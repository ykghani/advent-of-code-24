'''Advent of Code 2024 Day 13: Claw Contraption'''
from pathlib import Path
import numpy as np

script_dir = Path(__file__).parent
file_path = script_dir / 'd13.txt'

part_two_adjustment = 10_000_000_000_000

def parse_line(line: str):
    tmp = line.split(':')
    tmp2 = tmp[1].strip().split(',')
    a, b = int(tmp2[0].strip()[2: ]), int(tmp2[1].strip()[2:])
    return (a, b)

def part_one(a, b, p) -> int: 
    if 100 * a[0] + 100 * b[0] < p[0]:
        return 0
    if 100 * a[1] + 100 * b[1] < p[1]:
        return 0
    
    for i in range(1, 101):
        for j in range(1, 101):
            if a[0] * i + b[0] * j == p[0] and a[1] * i + b[1] * j == p[1]:
                return 3 * i + j
    
    return 0

def is_int_float(x, tol = 1e-3):
    return abs(x - round(x)) < tol

def part_two(a, b, p) -> int: 
    #Closed form solution found via mathamatical substitution method
    p = (p[0] + part_two_adjustment, p[1] + part_two_adjustment)
    
    B = (p[1] - (a[1]*p[0])/a[0]) * (a[0] / (a[0] * b[1] - a[1]* b[0]))
    A = (p[0] - B * b[0]) / a[0]
    
    if A >= 0 and B >= 0 and is_int_float(A) and is_int_float(B):
        return 3 * round(A) + round(B)
    else:
        return 0



total_tokens = 0
tokens2 = 0
with open(file_path, 'r') as f: 
    while True: 
        button_a = f.readline().strip()
        if not button_a:
            break 
        
        button_b = f.readline().strip()
        prize = f.readline().strip()
        
        f.readline() #Skips empty row 
        
        a = parse_line(button_a)
        b = parse_line(button_b)
        p = parse_line(prize)
        
        total_tokens += part_one(a, b, p)
        tokens2 += part_two(a, b, p)

print(f"Part one: {total_tokens}")
print(f"Part two: {tokens2}")