# Special Pythagorean Triplet
# There exists exactly one Pythagorean Triplet for which a + b + c = 1000.
# Find the product of abc

# brute force

max = 1000

for a in range(1, max):
    for b in range(a+1,max-a):
        c = 1000 - a - b

        if a**2 + b**2 == c**2:
            print(f"a = {a}, b = {b}, c = {c}")
            print(f"Product abc = {a*b*c}")