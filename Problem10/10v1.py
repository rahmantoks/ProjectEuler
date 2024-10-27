# Summation of Primes
# Find the sum of all primes below two million
# v1 improved using Sieve of Eratosthenes

import math

# Set maximum limit
max = 2000000

# Create a boolean array, initialized to True
is_prime = [True] * max

# 0 and 1 are not prime
is_prime[0] = is_prime[1] = False

# Implementing the Sieve of Eratosthenes
for num in range(2, int(math.sqrt(max)) + 1):
    if is_prime[num]:
        for multiple in range(num*num, max, num):
            is_prime[multiple] = False

# Summing all primes
sum = sum(i for i,prime in enumerate(is_prime) if prime)

print(sum)