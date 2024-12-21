#Advent of Code 2024 - Day 6 Bridge Repair

from pathlib import Path
from itertools import product

script_dir = Path(__file__).parent
file_path = script_dir / 'd7.txt'

funcs = {0: lambda x, y: x + y,
         1: lambda x, y: x * y,
         2: lambda x, y: int(''.join([str(x), str(y)]))}

def test(ans: int, cons: list, lim) -> int:     
    sequences = list(product(range(0, lim + 1), repeat= len(cons) - 1))
    pairs = list(zip(cons[:-1], cons[1: ]))
    
    for seq in sequences:
        result = cons[0]
        for i in range(len(seq)):
            result = funcs[seq[i]](result, cons[i + 1])
        
        if result == ans: 
            return ans
    return 0

part_one = part_two = 0
with open(file_path, 'r') as f: 
    for line in f: 
        line = line.strip().split(':')
        ans = int(line[0])
        cons = [int(i) for i in line[1].split()]
        
        part_one += test(ans, cons, 1)
        part_two += test(ans, cons, 2)
        
print(f"Part one: {part_one}")
print(f"Part two: {part_two}")