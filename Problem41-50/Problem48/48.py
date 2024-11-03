# Self Powers
# Find the last ten digits of the series 1^1 + 2^2 + 3^3 + 4^4 + .... + 1000^1000

import time
start = time.time()

sum_all = 0
last_ten = ""
for i in range(1, 1001):
    sum_all += i ** i

str_sum_all = str(sum_all)
print(str_sum_all[-10:])
end = time.time()
elapsed = end - start
print(f"elapsed time = {elapsed} seconds")
