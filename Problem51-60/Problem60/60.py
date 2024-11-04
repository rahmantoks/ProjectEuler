# Prime Pair Sets
import sympy

def concat_prime(p1,p2):
    concat1 = int(str(p1) + str(p2)) 
    concat2 = int(str(p2) + str(p1)) 

    return sympy.isprime(concat1) and sympy.isprime(concat2)

def find_set(primes, current_set, setsize=5):
    if len(current_set) == setsize:
        return current_set
    
    for prime in primes:
        if current_set and prime <= current_set[-1]:
            continue

        if all(concat_prime(prime, p) for p in current_set):
            new_set = find_set(primes, current_set + [prime], setsize)
            if new_set:
                return new_set
            
    return None

def solve():
    primes = list(sympy.primerange(2,10000))
    result = find_set(primes, [], 5)
    if result:
        print("Found prime set:", result)
        print("Sum:", sum(result))

solve()