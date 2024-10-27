# Non-Abundant Sums
# <p>A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.</p>
# <p>A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.</p>

# <p>As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.</p>
# <p>Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.</p>

import math

# Sum all proper divisor (from problem 21)
def sum_of_divisors(num):
    upper = int(math.sqrt(num)) + 1
    divisor_sum = 1
    for i in range(2, upper):
        if num % i == 0:
            divisor_sum+=i
            if i != num // i:
                divisor_sum += num // i 
    
    return divisor_sum

# Identify abundant numbers up to 28123
limit = 28123
abundant_numbers = [n for n in range(1, limit + 1) if sum_of_divisors(n) > n]

# Generate all sums of two abundant numbers up to limit
abundant_sums = set()
for i in abundant_numbers:
    for j in abundant_numbers:
        if i + j <= limit:
            abundant_sums.add(i+j)

# Find all integers up to limit that cannot be expressed as sums of abundant numbers
all_numbers = set(range(1, limit+1))
non_abundant_sums = all_numbers - abundant_sums

sum_non_abundant = sum(non_abundant_sums)

print(sum_non_abundant)