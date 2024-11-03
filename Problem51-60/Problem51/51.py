# Prime Digit Replacements
import math
import time
import itertools

start = time.time()

def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i + i, limit + 1, i):
                sieve[j] = False
            
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def replace_digits(number, mask_digit_positions):
    """Replaces specific positions in the number with '*' to create a pattern."""
    num_str = list(str(number))
    for pos in mask_digit_positions:
        num_str[pos] = '*'
    return ''.join(num_str)

def find_smallest_prime_with_eight_prime_family(limit):
    primes = generate_primes(limit)
    prime_set = set(primes)  # Set for quick prime checks
    
    for prime in primes:
        str_prime = str(prime)
        length = len(str_prime)
        
        # Try all combinations of positions to replace
        for num_replacements in range(1, length):
            for positions in itertools.combinations(range(length), num_replacements):
                pattern = replace_digits(prime, positions)
                
                prime_family = []
                # Replace '*' in pattern with digits 0-9
                for digit in '0123456789':
                    candidate = int(pattern.replace('*', digit))
                    if candidate in prime_set and len(str(candidate)) == length:
                        prime_family.append(candidate)
                
                # Check if the family contains exactly 8 primes
                if len(prime_family) == 8:
                    return min(prime_family), prime_family

# Parameters
LIMIT = 1000000

# Find the result
result_prime, result_family = find_smallest_prime_with_eight_prime_family(LIMIT)
print(result_prime)
print(result_family)