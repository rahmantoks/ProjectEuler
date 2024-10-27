import math
# Find the 10001st prime number
target = 10001
current = 3

prime = [2]

# check if prime 
def isprime(num):
    # use limit because divisor always come in pairs
    limit = int(math.sqrt(num)) + 1
    for i in prime:
        if i > limit:
            break
        if num % i == 0:
            return False
    return True

# Search the target-th prime
while len(prime) < target:
    if isprime(current):
        prime.append(current)
    
    # iterate by 2 because even number can't be prime
    current +=2

print(prime[-1])