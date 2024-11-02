# Pentagon Numbers
import math

def pentagon_n(n):
    return int(n * (3*n - 1) / 2)

# Function to check if a number is pentagonal
def is_pentagonal(x):
    # Solve the quadratic equation to check if x is pentagonal
    n = (1 + math.sqrt(1 + 24 * x)) / 6
    return n.is_integer()

min_d = float("inf")
result_pair = None
limit = 3000

pentagonals = [pentagon_n(n) for n in range(1,limit)]

for j in range(1,limit ):
    for k in range(j+1, limit):
        P_j = pentagonals[j-1]
        P_k = pentagonals[k-1]

        sums = P_j + P_k
        diff = P_k - P_j

        if is_pentagonal(sums) and is_pentagonal(diff):
            if diff < min_d:
                min_d = diff
                result_pair = (P_j, P_k)


print(min_d, result_pair)