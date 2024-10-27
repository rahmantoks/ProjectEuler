# Number Letter Counts
# If all numbers from 1 to 1000 (one thousand) inclusive were written ouot in words, how many letters would be used?
def num_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 1000:
        return "onethousand"

    words = ""
    if n >= 100:
        words += ones[n // 100] + "hundred"
        if n % 100 != 0:
            words += "and"
        n %= 100

    if n >= 20 or n == 10:
        words += tens[n // 10]
        n %= 10
    elif 10 < n < 20:
        words += teens[n - 10]
        return words

    words += ones[n]
    return words

# Calculate the total number of letters used from 1 to 1000
total_letters = sum(len(num_to_words(n)) for n in range(1, 1001))

print(total_letters)