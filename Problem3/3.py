# The prime factors of 13195 are 5,7,13 and 29
# What is the largest prime factor of the number 600851475143

def largest_prime(n):
    i = 2

    while i * i <= n:
        if n % i == 0:
            n = n / i
        else:
            i = i + 1
    
    return n

target = 600851475143

print(largest_prime(target))