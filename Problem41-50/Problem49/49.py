# Prime Permutations


import math
import time
from itertools import permutations

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
PRIME_LIMIT = 10000
SEEK_LIMIT = 9876

# Generate primes
primes = generate_primes(PRIME_LIMIT)
set_primes = set(primes)

# Prime groups
prime_groups = {}

for prime in primes:
    if len(str(prime)) < 4:
        continue

    key = ''.join(sorted(str(prime)))
    if key not in prime_groups:
        prime_groups[key] = []

    prime_groups[key].append(prime)

for key, primes in prime_groups.items():
    if len(primes) < 3:
        continue

    primes.sort()
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            diff = primes[j] - primes[i]
            third = primes[j] + diff
            if third in primes:
                sequence = [primes[i], primes[j], third]
                print(sequence)
                print(f"{primes[i]}{primes[j]}{third}")
