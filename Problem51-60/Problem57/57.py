# Square Root Converges

from fractions import Fraction

count = 0
fracs = {0:0}

def get_fraction(n):
    if n not in fracs:
        fracs[n] = Fraction(1, 2 + get_fraction(n-1))
  
    return fracs[n]

count = 0
for i in range(1,1000):
    result = 1 + get_fraction(i)
    num_digit = len(str(result.numerator))
    denom_digit = len(str(result.denominator))

    if num_digit > denom_digit:
        count+=1

print(count)