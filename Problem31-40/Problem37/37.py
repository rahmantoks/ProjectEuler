# Truncatable Primes
# The numbere 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage
# 3797, 797, 97, 7. Similarly we can work from right to left:
# 3797, 379, 37, 7.
import math
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# Sieve of erothesenes

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def create_primes(limit):
    """Create a list of primes using the Sieve of Eratosthenes up to the given limit."""
    prime_arr = [True] * (limit + 1)
    prime_arr[0] = prime_arr[1] = False  # 0 and 1 are not primes
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime_arr[i]:
            for n in range(i*i, limit + 1, i):
                prime_arr[n] = False
    return {i for i, is_prime in enumerate(prime_arr) if is_prime}

def is_truncatable(prime, prime_set):
    """Check if a prime is truncatable from both left to right and right to left."""
    prime_str = str(prime)
    
    # Check left to right truncation
    for i in range(1, len(prime_str)):
        if int(prime_str[i:]) not in prime_set:
            return False

    # Check right to left truncation
    for i in range(1, len(prime_str)):
        if int(prime_str[:-i]) not in prime_set:
            return False
    
    return True

# Define the limit and create the set of primes
LIMIT = 1000000
primes = create_primes(LIMIT)

# Skip digits that would make truncation impossible (0, 4, 6, 8)
skip_digits = set("0468")
truncatable_primes = []

# Find all truncatable primes
for prime in primes:
    if prime < 10:
        continue  # Skip single-digit primes

    prime_str = str(prime)
    if skip_digits.intersection(prime_str):
        continue  # Skip primes containing 0, 4, 6, or 8

    if is_truncatable(prime, primes):
        truncatable_primes.append(prime)

# Output the result
print(f"Number of truncatable primes: {len(truncatable_primes)}")
print(f"Truncatable primes: {truncatable_primes}")
print(f"Sum of truncatable primes: {sum(truncatable_primes)}")