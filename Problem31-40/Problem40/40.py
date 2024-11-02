# Champernowne's Constant
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415...
# it can be seen that the 12-th digit of the fractional part is 1.
# if dn is the nth digit of the fractional part 
# find d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

# limit 
max_target = 1000000
frac = ""
n = 1  
while len(frac) < max_target:
    frac += str(n)
    n+=1

product = 1
for i in range(0,6):
    product *= int(frac[10 ** i - 1])

print(product)
