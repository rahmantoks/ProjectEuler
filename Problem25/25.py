# 1000-digit Fibonacci Number
# What is the index of the first term in the Fibonacci sequence to contain digits?]

memo = {
    1:1,
    2:1
}

def fibonaci(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonaci(n-1) + fibonaci(n-2)
        return memo[n]

n = 1
while True:
    if len(str(fibonaci(n))) >= 1000:
        break
    
    n+=1

print(n)