# Number Letter Counts
# If all numbers from 1 to 1000 (one thousand) inclusive were written ouot in words, how many letters would be used?

ones_word = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}

tens_word = {
    1 : "ten",
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety"
}

special_word = {
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
}

def words_from_num(num):
    words = ""
    thousands = num // 1000
    num -= thousands * 1000
    hundreds = num // 100
    num -= hundreds * 100
    tens = num // 10
    ones = num - tens * 10 

    if thousands > 0:
        words += ones_word.get(thousands) 
        words += "thousand"
    if hundreds > 0:
        words += ones_word.get(hundreds)
        words += "hundred"
    if (thousands > 0 or hundreds > 0) and (tens > 0 or ones > 0):
        words += "and" 
    if tens > 0:
        if tens == 1 and ones > 0:
            words += special_word.get(tens * 10 + ones)
            return words
        else:
            words += tens_word.get(tens, "")
    if ones > 0:
        words += ones_word.get(ones)

    return words

all_words = ""
for n in range(1,1000+1):
    all_words += words_from_num(n)

print(len(all_words))
    
