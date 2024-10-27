# Summation of Primes
# Find the sum of all primes below two million
import math

current = 3
prime = [2]
sum = 2
max = 2000000

# check if prime 
def isprime(num):
    # use limit because divisor always come in pairs
    limit = int(math.sqrt(num)) + 1
    for i in prime:
        if i > limit:
            break
        if num % i == 0:
            return False
    return True

# Search the target-th prime
while current < max:
    if isprime(current):
        prime.append(current)
        sum += current
    
    # iterate by 2 because even number can't be prime
    current +=2

print(sum)