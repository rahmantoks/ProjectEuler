# What is the sum of the digits of the number 2^1000 ?

number = 2 ** 1000
digits = str(number)

sum = 0
for num in digits:
    sum += int(num)

print(sum)