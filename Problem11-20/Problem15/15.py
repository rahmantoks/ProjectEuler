# Lattice Paths
# Starting in the top left corner of 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right.
# How many such routes are there through a 20 x 20 grid

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combination(n,r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print (combination(40,20))
