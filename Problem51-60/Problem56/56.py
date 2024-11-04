# Powerful Digital Sum
# Considering natural numbers of the form, a^b, where a,b < 100, what is the maximum digital sum?

maximum = 0

def digital_sum(num):
    return sum(int(digit) for digit in num)

for a in range(1,100):
    for b in range(1,100):
        calc_result = a**b 
        digit_sum = digital_sum(str(calc_result))
        if digit_sum > maximum:
            maximum = digit_sum

print(maximum)
        