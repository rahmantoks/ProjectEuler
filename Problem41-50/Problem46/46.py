# Goldbach's Other Conjecture
# Christian Goldbach proposed that every odd composite number can be written as the sum of prime and twice a square
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of the prime and twice a square

import math

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i + i, limit + 1, i):
                sieve[j] = False
            
    return [num for num, is_prime in enumerate(sieve) if is_prime]

# Set reasonable limit
LIMIT = 10000

# Generate primes
primes = generate_primes(LIMIT)
set_primes = set(primes)

# Loop Through Odd Composite number
for comp in range(9, LIMIT, 2):
    if comp in set_primes:
        continue

    found = False
    for prime in primes:
        if prime >= comp:
            break

        remaining = comp - prime
        if remaining % 2 == 0:
            square_part = math.isqrt(remaining // 2)
            if square_part * square_part == remaining // 2:
                found = True
                break
        
    if not found:
        print(comp)
        break        