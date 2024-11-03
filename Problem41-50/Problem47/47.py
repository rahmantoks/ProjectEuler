# Distinct Primes Factors
# The first two consecutive numbers to have two distinct prime factors are 14 and 15
# The first three consecutive numberes to have three distinct prime factors are 644, 655, 646
# Find the first four consecutive numbers to have four distinct prime factor each. What is the first of these numbers.

import math
import time

start_time = time.time()

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i + i, limit + 1, i):
                sieve[j] = False
            
    return [num for num, is_prime in enumerate(sieve) if is_prime]

# Set reasonable limit
LIMIT = 1000000

# Generate primes
primes = generate_primes(LIMIT)
set_primes = set(primes)

# Get distinct prime factors
def get_distinct_prime_factors(num):
    factors = set()
    for prime in primes:
        if prime * prime > num:
            break
        while num % prime == 0:
            factors.add(prime)
            num //= prime

    if num > 1:
        factors.add(num)

    return factors

# Check if consecutive number has 4 distinct prime factors
def have_four_distinct_factors(num):
    if len(get_distinct_prime_factors(num)) != 4:
        return False
    if len(get_distinct_prime_factors(num+1)) != 4:
        return False
    if len(get_distinct_prime_factors(num+2)) != 4:
        return False
    if len(get_distinct_prime_factors(num+3)) != 4:
        return False
    return True

# Loop for each number to limit
for i in range(210, LIMIT):
    if have_four_distinct_factors(i):
        print(i)
        break

end_time = time.time()
elapsed_time = end_time - start_time
print(f"elapsed time = {elapsed_time} seconds.")