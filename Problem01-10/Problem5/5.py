# 2520 is the smalles number that can be divided by each of the numers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

start = 2520
found = False

while not found:
    result = True
    for i in range(20,1,-1):
        if start % i != 0:
            result = False
            break
    
    if result:
        found = True
    else:
        start = start + 1

print(start)