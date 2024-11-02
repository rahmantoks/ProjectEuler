# Triangular, Pentagonal, and Hexagonal
# It can be verivied that 40755 is triangular pentagonal and hexagonal
# Find the next triangle number thtat is also pentagonal and hexagonal

import math

def istriangle(num):
    n = (-1 + math.sqrt(1 + 8 * num)) / 2
    return n.is_integer()

def ispentagonal(num):
    n = (1 + math.sqrt(1 + 24 * num)) / 6
    return n.is_integer()

def ishexagonal(num):
    n = (1 + math.sqrt(1 + 4 * num)) / 4
    return n.is_integer()

n = 143
while True:
    n += 1
    check = n * (2 * n - 1)
    print(f"checking {check}")

    if not ispentagonal(check):
        continue
    if not istriangle(check):
        continue
    
    print(check)
    break
