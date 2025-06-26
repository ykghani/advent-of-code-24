'''Advent of Code 2024 Day 13: Claw Contraption'''
from pathlib import Path
from sympy import diophantine, symbols, Symbol, solve

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

def part_two(a, b, p) -> int: 
    p = list(p)
    p[0] += part_two_adjustment
    p[1] += part_two_adjustment
    
    x, y = symbols('x y') 
    eq1 = a[0]*x + a[1]*y - p[0]
    print(f"eq1: {eq1}")
    
    x_sol, y_sol = next(iter(diophantine(eq1)))
    print(f"x_sol: {x_sol}")
    print(f"y_sol: {y_sol}")
    
    eq2_subbed = b[0]*x_sol + b[1]*y_sol - p[1]
    print(f"eq2_subbed: {eq2_subbed}")
    
    # For equation in form: at + b = 0
    # Manually extract coefficient and constant
    from sympy import collect
    t = Symbol('t_0')
    eq_collected = collect(eq2_subbed, t)
    print(f"eq_collected: {eq_collected}")
    
    # Extract coefficient of t and constant term
    coeff = eq_collected.coeff(t, 1)  # Get coefficient of t^1
    const = eq_collected.coeff(t, 0)  # Get constant term
    print(f"coefficient: {coeff}, constant: {const}")
    
    # Solve: at + b = 0 -> t = -b/a
    t_sol = -const / coeff
    print(f"t_sol: {t_sol}")
    
    x_val = int(x_sol.subs(t, t_sol))
    y_val = int(y_sol.subs(t, t_sol))
    
    return 3*x_val + y_val
    

print(part_two((94, 34), (22, 67), (8400, 5400)))
# print(part_one((26, 66), (67, 21), (12748, 12176)))
# print(part_one((17, 86), (84, 37), (7870, 6450)))


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
        

# def forward_eea(a: int, b: int):
#     remainders = [a]
#     quotients = []
    
#     while b != 0:
#         quotient = a // b
#         remainder = a % b
        
#         remainders.append(b)
#         quotients.append(quotient)
        
#         a, b = b, remainder
    
#     return remainders, quotients

# def backwards_eea(remainders, quotients):
#     s2, s1 = 1, 0  # Coefficients for first number
#     t2, t1 = 0, 1  # Coefficients for second number
    
#     for q in reversed(quotients):
#         s = s2 - q * s1
#         t = t2 - q * t1
        
#         s2, s1 = s1, s
#         t2, t1 = t1, t
    
#     return s2, t2


# def eea(a, b):
#     remainders, quotients = forward_eea(a, b)
#     gcd_val = remainders[-1]
#     s, t = backwards_eea(remainders, quotients)
#     return gcd_val, s, t

# def solve_equation(v1, v2, c):
#     a1, b1 = v1
#     a2, b2 = v2
    
#     d = gcd(a1, b1)
#     if c[0] % d != 0:
#         raise ArithmeticError("No integer solution exists")
    
#     _, s, t = eea(a1, b1)
#     scale = c[0] // d
#     x0 = s * scale
#     y0 = t * scale
    
#     coef = a2 * (b1 // d) - b2 * (a1 // d)
#     if coef == 0:
#         raise ArithmeticError("Coefficient for k is zero")
    
#     k = (c[1] - a2 * x0 - b2 * y0) // coef
    
#     x = x0 + (b1 // d) * k
#     y = y0 - (a1 // d) * k
#     return (x, y)

# def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
#     """
#     Returns (gcd, s, t) where gcd is the greatest common divisor of a and b
#     and s, t are coefficients such that gcd = s*a + t*b
#     """
#     # Initialize the coefficients for the first two numbers
#     old_s, s = 1, 0        # Coefficients for a
#     old_t, t = 0, 1        # Coefficients for b
#     old_r, r = a, b        # The remainders

#     while r != 0:
#         # Compute quotient and update remainders
#         quotient = old_r // r
#         old_r, r = r, old_r - quotient * r

#         # Update coefficients for a
#         old_s, s = s, old_s - quotient * s

#         # Update coefficients for b
#         old_t, t = t, old_t - quotient * t

#     # When r becomes 0, old_r is the GCD, and (old_s, old_t) are the coefficients
#     return old_r, old_s, old_t


# def solve_eqn(a1, b1, c1, a2, b2, c2):
#     gcd, s, t = extended_gcd(a1, b1)
    
#     if c1 % gcd != 0:
#         raise ArithmeticError("Doesn't divide cleanly by GCD, non-integer result")
    
#     scale = c1 // gcd
#     x0 = s * scale
#     y0 = t * scale
    
#     #General solution to first equation
#     # x = x0 + (b1 / gcd) * k 
#     # y = y0 + (a1 / gcd) * k
    
#     #Sub into equation 2
#     # a2(x0 + (b1/gcd1)k) + b2(y0 - (a1/gcd1)k) = c2
#     k = (c2 - a2*x0 - b2*y0) * gcd // (a2 * b1 + b2)
    
#     x = x0 + (b1//gcd)*k
#     y = y0 - (a1//gcd)*k
    
#     return (x, y)




        
        # print(parse_line(button_a))

# print(solve_equation((94, 34), (22, 67), (8400, 5400)))
# print(solve_linear_system(94,34,8400, 22, 67, 5400))
# print(extended_gcd(252, 198))
# print(4*252 + (-5)*198)
# print(extended_gcd(94, 34))
# print(solve_eqn(94, 34, 8400, 22, 67, 5400))