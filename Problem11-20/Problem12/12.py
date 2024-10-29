# Highly Divisible Triangular Number
# What is the value of the first triangle number to have over five hundred divisor

import math

maxdiv = 500
tri = 0
n = 1
# Get nth triangle
def triangle(num):
    sum = 0
    for i in range(num+1):
        sum+=i
    return sum

# get the number of divisor
def numofdiv(num):
    count = 0
    max = int(math.sqrt(num))
    for i in range(1,max):
        if num % i == 0:
            count+=2 # i and num/i are pair
    
    # adjust for perfect square
    if max * max == num:
        count-=1
    
    return count

while True:
    tri = triangle(n)
    div = numofdiv(tri)
    if div > maxdiv:
        print(tri)
        break
    n += 1