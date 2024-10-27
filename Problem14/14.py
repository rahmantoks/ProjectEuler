# Longest Collats Sequance
start_max = 1000000
max_start = 0
max_chain = 0

def collatz_sequence_length(n, memo):
    original = n
    length = 0

    # Calculate sequence length using memoization
    while n != 1:
        if n < len(memo) and memo[n] != 0:
            length += memo[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1

    # Memoize the length for the original number
    if original < len(memo):
        memo[original] = length

    return length

# Create a memoization array to store chain lengths
memo = [0] * start_max

# Loop through all numbers below start_max
for i in range(2, start_max):
    length = collatz_sequence_length(i, memo)
    if length > max_chain:
        max_chain = length
        max_start = i

print(max_start)
