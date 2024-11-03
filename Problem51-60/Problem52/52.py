# Permuted Multiples
# find the smallest positive integer x such as that 2x 3x 4x 5x and 6x contain the same digits

def get_digits(num):
    digits = [digit for digit in str(num)]
    digits.sort()

    return ''.join(digit for digit in digits)

start = 1000
limit = 999999

for num in range(start, limit):
    key = get_digits(num)

    if get_digits(6 * num) != key:
        continue
    if get_digits(5 * num) != key:
        continue
    if get_digits(4 * num) != key:
        continue
    if get_digits(3 * num) != key:
        continue
    if get_digits(2 * num) != key:
        continue

    print(num)
    break

