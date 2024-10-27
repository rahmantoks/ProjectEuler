# Find the 10001st prime number
target = 10001
current = 3

prime = [2]

# Check if odd
def isodd(num):
    if num % 2 == 0:
        return False
    else:
        return True

# check if prime 
def isprime(num):
    for i in prime:
        if num % i == 0:
            return False

    return True

# Search the target-th prime
while True:
    if isodd(current):
        if isprime(current):
            prime.append(current)
            if len(prime) == target:
                break
    current += 1

print(prime[target-1])