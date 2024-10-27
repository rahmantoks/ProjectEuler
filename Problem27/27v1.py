# Quadratic Primes
# v1 Improved
# Precompute primes using sieve of erathosthenes
# Restrinct a to odd number and b to primes
import math

# Sieve of Eratosthenes to generate primes up to a limit
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes, is_prime

# Precompute primes up to 10,000 (a safe upper limit for this problem)
primes, is_prime = sieve(100000)

# Function to check the length of prime sequence for given a and b
def check_longest_prime(a, b):
    n = 0
    while True:
        num = n * n + a * n + b
        if num < 0 or not is_prime[num]:
            break
        n += 1
    return n

max_count = 0
max_product = 0

# Restrict b to positive primes less than 1000
for b in primes:
    if b > 1000:
        break
    # Check both positive and negative values of a
    for a in range(-999, 1000, 2):  # Only odd values of a
        prime_count = check_longest_prime(a, b)
        if prime_count > max_count:
            max_count = prime_count
            max_product = a * b

print(max_product)