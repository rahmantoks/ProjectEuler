# Sub-string Divisibility

from itertools import permutations

sum_all = 0
for num in permutations("0123456789"):
    str_num = ''.join(num)
    if int(str_num[1:4]) % 2 != 0:
        continue
    if int(str_num[2:5]) % 3 != 0:
        continue
    if int(str_num[3:6]) % 5 != 0:
        continue
    if int(str_num[4:7]) % 7 != 0:
        continue
    if int(str_num[5:8]) % 11 != 0:
        continue
    if int(str_num[6:9]) % 13 != 0:
        continue
    if int(str_num[7:10]) % 17 != 0:
        continue

    sum_all += int(str_num)

print(sum_all)