# Lychrel Numbers

def ispalindrom(num):
    return str(num) == str(num)[::-1]

def islychrel(num):
    reversed_num = str(num)[::-1]
    if ispalindrom(num + int(reversed_num)):
        return True
    else:
        return False

def count_lychrel_num(limit):
    count = 0
    for num in range(1,limit+1):
        num_reversed = int(str(num))
        if ispalindromic(num + num_reversed):
            count+=1

print(ispalindromic(1002))