# Double-base Palindromes
# The decimal number 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# check palindrome for int
def check_palind_decimal(num):
    str_num = str(num)
    length = len(str_num)
    if length == 1:
        return True
    
    for i in range(length//2):
        if str_num[i] != str_num[length-i-1]:
            return False
    return True

# check palindrome for string
def check_palind_string(string):
    length = len(string)
    if length == 1:
        return True
    
    for i in range(length//2):
        if string[i] != string[length-i-1]:
            return False
    return True

# convert decimal to binary
def dec_to_bin(num):
    binnary = []
    while num > 0:
        remainder = num % 2
        binnary.append(remainder)
        num = num // 2

    return "".join(str(x) for x in binnary[::-1])

maximum = 1000000
target_decimal = []
target=[]
for num in range(maximum):
    if check_palind_decimal(num):
        target_decimal.append(num)

for num in target_decimal:
    if check_palind_string(dec_to_bin(num)):
        target.append(num)


print(sum(target))