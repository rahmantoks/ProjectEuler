# Spiral Primes
from sympy import isprime

def find_spiral_side_length(target_ratio):
    side_length = 1
    prime_count = 0
    total_diagonal_numbers = 1  # Start with the center (1), which is not prime

    while True:
        side_length += 2  # Increase the side length by 2 for each new layer
        corners = [
            side_length**2,                        # Bottom-right corner
            side_length**2 - (side_length - 1),    # Bottom-left corner
            side_length**2 - 2 * (side_length - 1),  # Top-left corner
            side_length**2 - 3 * (side_length - 1)   # Top-right corner
        ]
        
        # Count primes among the new corner numbers
        prime_count += sum(1 for corner in corners if isprime(corner))
        total_diagonal_numbers += 4  # Four new diagonal numbers are added
        
        # Calculate the ratio of primes to total diagonal numbers
        prime_ratio = prime_count / total_diagonal_numbers
        
        # Check if the ratio falls below the target ratio
        if prime_ratio < target_ratio:
            return side_length

# Find the side length where the ratio of primes along diagonals first falls below 10%
target_ratio = 0.1
result = find_spiral_side_length(target_ratio)
print(result)
