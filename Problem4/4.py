# A palindromic number reads the same both ways.
# The largest palindrome made from the product of 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.

min = 100
max = 999
biggest = 0

def ispalindrome(n):
    ori = str(n)
    rev = ori[::-1]
    return ori == rev

for i in range(min, max):
    for j in range(min, max):
        num = i * j
        if ispalindrome(num):
            if num > biggest:
                biggest = num

print(biggest) 