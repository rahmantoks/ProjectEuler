# Circular Primes
# The number 197 is called circular prime because all rotations f the digits:
# 197, 917, 719 are themselves prime.
# There are thirteen such primes below 100:
# 2,3,5,7,11,13,17,31,37,71,73,79,97
# Howmany circular primes are there below one million
import math

# Sieve of erothesenes

def isprime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
        
    return True

def createprimes(limit):
    maximum = limit
    prime_arr = [True] * (maximum + 1)
    i = 2
    while i * i <= maximum:
        if prime_arr[i]:
            for n in range(i*i, maximum + 1, i):
                prime_arr[n] = False
        
        i+=1
    
    primes = [i for i in range(2,maximum+1) if prime_arr[i]]
    return primes



# max = 1000000
maximum = 1000000
primes = set(createprimes(maximum))


target = []

def rotate_digits(num):
    # Convert the number to a string
    num_str = str(num)
    n = len(num_str)
    rotations = []
    
    # Generate all rotations
    for i in range(n):
        # Rotate by slicing and concatenating
        rotation = num_str[i:] + num_str[:i]
        # Convert back to integer and add to the list
        rotations.append(int(rotation))
        
    return rotations

for num in primes:
    print(f"checking {num}")
    str_num = str(num)
    if str_num != '2':
        if '0' in str_num or '2' in str_num or '4' in str_num or '6' in str_num or '8' in str_num:
            continue

    rotated_list = rotate_digits(num)
    
    add = True
    for item in rotated_list:
        if int(item) not in primes:
            add = False
            break

    if add :
        target.append(num)

print(target)
print(len(target))
    
