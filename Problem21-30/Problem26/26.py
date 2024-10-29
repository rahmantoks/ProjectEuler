# Reciprocal Cycles
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part

def check_cycle(d):
    remainders = {}
    remainder = 1
    position = 0

    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        
        remainders[remainder] = position

        remainder = (remainder) * 10 % d
        position += 1

    return 0

max_cycle = 0
max_d = 0

for d in range(2,1001):
    current_cycle = check_cycle(d)

    if current_cycle > max_cycle:
        max_cycle = current_cycle
        max_d = d

print(max_d)