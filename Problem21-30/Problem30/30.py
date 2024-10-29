# Digit Fifth Powers
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

fifthpower = {}

for x in range(0,10):
    fifth = x ** 5
    fifthpower[x] = fifth

# largest possible sum for 6 digits = 999999 = 354294 
max_limit = 6 * fifthpower.get(9)
total_sum = 0
for i in range(2,max_limit):
    sum_of = sum(fifthpower[int(digit)] for digit in str(i))
            
    if sum_of == i:
        total_sum += sum_of

print(total_sum)