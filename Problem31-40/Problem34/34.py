# Digit Factorial
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

factorial_table = {}

for i in range(0,10):
    factorial_table[i] = factorial(i)

max_limit = 7 * factorial_table.get(9)

target = []
for number in range(10,max_limit):
    str_number = str(number)
    digit_fact_sum = 0
    for digit in str_number:
        digit_fact_sum += factorial_table.get(int(digit))
    
    if number == digit_fact_sum:
        target.append(number)

print(sum(target))