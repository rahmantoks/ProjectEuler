# Lychrel Numbers

def ispalindrom(num):
    return str(num) == str(num)[::-1]

def count_lychrel_num(limit):
    count = 0
    for num in range(1,limit+1):
        iterations = 0
        found = False
        curr_num = num
        while iterations < 50 and not found:
            curr_num_reversed = int(str(curr_num)[::-1])
            check_num = curr_num + curr_num_reversed
            if ispalindrom(check_num):
                found = True
            else:
                curr_num = check_num
            
            iterations += 1
        
        if not found:
            count+=1
    
    return count

limit = 10000
print(count_lychrel_num(limit))
