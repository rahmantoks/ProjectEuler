# Consecutive Prime Sum

import math
import time

start = time.time()

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i + i, limit + 1, i):
                sieve[j] = False
            
    return [num for num, is_prime in enumerate(sieve) if is_prime]

# Set reasonable limit
PRIME_LIMIT = 1000000
SUM_LIMIT = 1000000

# Generate primes
primes = generate_primes(PRIME_LIMIT)
set_primes = set(primes)

num_primes = len(primes)
max_length = 0
max_prime = 0
for i in range(num_primes):
    sum_total = 0
    for j in range(i, num_primes):
        sum_total += primes[j]
        if sum_total > SUM_LIMIT:
            break
        if sum_total in set_primes and (j - i + 1) > max_length:
            max_length = j - i + 1
            max_prime = sum_total
    
print(max_prime, max_length)

