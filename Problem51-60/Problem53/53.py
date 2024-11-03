# Combinatorial Selection
# How many nCr for 1<= n <= 100 are greater than one-million

factorials = {
    0:1,
    1:1
    }

def factorial(n):
    if n in factorials:
        return factorials[n]    
    else:
        factorials[n] = n * factorial(n-1)
        return factorials[n]

def combination(n,r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))


def combination_greater_than_one_million():
    count = 0

    for n in range(1, 101):
        for r in range(1, n + 1):
            if combination(n,r) > 1000000:  
                count+=1    

    return count

print(combination_greater_than_one_million())