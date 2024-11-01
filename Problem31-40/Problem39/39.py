# Integer Right Triangles

p = 3
max_p = 0
max_count = 0

while p <= 1000:
    count = 0 
    for a in range(1,p//2):
        for b in range (a,(p-a)//2):
            c = p - a - b
            if a**2 + b**2 == c**2:
                count+=1
    
    if count > 0 and count > max_count:
        max_count = count
        max_p = p

    p+=1

print(f"for p:{max_p} count:{max_count}")