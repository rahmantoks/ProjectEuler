# Lexicographic Permutations

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

target = 1000000

digits = [0,1,2,3,4,5,6,7,8,9]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def lexicographic_permutation(digits, position):
    result = []
    available_digits = digits[:]
    position -= 1

    while available_digits:
        n = len(available_digits)
        fact_res = factorial(n-1)
        index = position // fact_res
        result.append(available_digits.pop(index))
        position %= fact_res

    return result

target_number = lexicographic_permutation(digits, target)
str_target_number = ''.join(str(x) for x in target_number)

print(str_target_number)


