# Factorial Digit Sum
# Find the sum of the digits in the number 100!

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

digits = str(factorial(100))

res = 0
for num in digits:
    res+=int(num)

print(res)