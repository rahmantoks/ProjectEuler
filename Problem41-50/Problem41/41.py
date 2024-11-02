# Pandigital Prime
#
# Sieve of erothesenes
import math

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

def ispandigital(num):
    str_num = str(num)
    if len(str_num) > 9:
        return False
    
    for i in range(1,len(str_num)+1):
        if str(i) not in str_num:
            return False

    return True

primes = createprimes(987654321)

for prime in primes[::-1]:
    if ispandigital(prime):
        print(prime)
        break
