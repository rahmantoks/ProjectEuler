# Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

thirtys = [4,6,9,11]
thirtyones = [1,3,5,7,8,10,12]
feb = [2]

days = {
    1:"Mon",
    2:"Tue",
    3:"Wed",
    4:"Thu",
    5:"Fri",
    6:"Sat",
    7:"Sun"
}

count = 0
currentday = 2

for year in range(1901,2001):
    for month in range(1, 13):
        if currentday == 7:
            count+=1
        
        if month in thirtyones:
            daysinmonth = 31
        elif month in thirtys:
            daysinmonth = 30
        elif month in feb:
            # Leap year check
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                daysinmonth = 29
            else:
                daysinmonth = 28
        
        # move to first day of next month
        currentday = (currentday + daysinmonth) % 7

        # if no remainder (feb:28day) its the sameday
        if currentday == 0:
            currentday = 7

print(count)