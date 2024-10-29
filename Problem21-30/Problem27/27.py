# Quadratic Primes

import math

# Check if prime
def isprime(num):
    if num < 2:
        return False
    # use limit because divisor always come in pairs
    limit = int(math.sqrt(num)) + 1
    for i in range(2,limit):
        if num % i == 0:
            return False
        
    return True

def check_longest_prime(a,b):
    prime_count = 0
    n = 0
    while True:
        num = n ** 2 + a * n + b
        if not isprime(num):
            break
        n+=1
        prime_count+=1

    return prime_count

max_count = 0 
max_product = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        if isprime(b):  
            prime_count = check_longest_prime(a,b)
            if prime_count > max_count:
                max_count = prime_count
                max_product = a * b

print(max_product)