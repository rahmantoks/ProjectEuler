# Pandigital Multiple

maximum = 99999
current_max = 0

def get_max_product(num):
    multiplier = 1
    product = ""
    while True:
        product += str(num * multiplier)
        if len(product) >= 9:
            break
        multiplier += 1
    
    return product
    

def ispandigital(string):
    if len(string) > 9:
        return False
    
    if '0' in string:
        return False
    
    seen = []
    for digit in list(string):
        if digit in seen:
            return False
        
        seen.append(digit)
    
    return True

for i in range(1,maximum):
    max_product = get_max_product(i)
    if ispandigital(max_product):
        new_max = int(max_product) 
        if new_max > current_max:
            current_max = new_max

print(current_max)
