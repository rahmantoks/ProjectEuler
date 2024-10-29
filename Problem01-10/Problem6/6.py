# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Find the sum of squares
def sumofsquare(num):
    return sum(i**2 for i in range(1, num + 1))

# Find the square of the sum
def squareofsum(num):
    total = sum(range(1, num+1))
    return total**2

# Find the difference
def calculate(num):
    return abs(sumofsquare(num) - squareofsum(num))

print(calculate(100))
