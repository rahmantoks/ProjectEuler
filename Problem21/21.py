# Amicable Numbers

import math

max_limit = 10000
amic_numbers = []
total_sum = 0

def sum_of_divisors(num):
    upper = int(math.sqrt(num)) + 1
    divisor_sum = 1
    for i in range(2, upper):
        if num % i == 0:
            divisor_sum+=i
            if i != num // i:
                divisor_sum += num // i 
    
    return divisor_sum

for i in range(2,max_limit+1):
    if i in amic_numbers:
        continue
    
    pair = sum_of_divisors(i)

    if pair == i:
        continue

    if sum_of_divisors(pair) == i:
        amic_numbers.append(i)
        amic_numbers.append(pair)
        total_sum += i
        total_sum += pair
    
print(total_sum)