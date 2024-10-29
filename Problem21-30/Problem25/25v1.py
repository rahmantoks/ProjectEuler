# 1000-digit Fibonacci Number
# What is the index of the first term in the Fibonacci sequence to contain digits?]
# v1 Optimized
# Use simple iteration, only remember the last 2 number

# Initial values for the Fibonacci sequence
a, b = 1, 1
n = 2

# Loop until we find a Fibonacci number with 1000 digits
while len(str(b)) < 1000:
    a, b = b, a + b
    n += 1

print(n)
