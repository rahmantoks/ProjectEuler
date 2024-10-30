# Digit Cancelling Fractions 
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectyl believe that 49/98 = 4/8 which is correct
from fractions import Fraction

target = []

for numerator in range(10,100):
    for denominator in range(numerator + 1,100):
        num_str = str(numerator)
        denom_str = str(denominator)

        common = set(num_str) & set(denom_str)

        if len(common) == 0 or '0' in common:
            continue

        common_digit = common.pop()

        new_num_str = num_str.replace(common_digit, '',1)
        new_denom_str = denom_str.replace(common_digit, '', 1)

        if new_num_str and new_denom_str:
            new_numerator = int(new_num_str)
            new_denominator = int(new_denom_str)

            if new_denominator != 0 and Fraction(numerator, denominator) == Fraction(new_numerator, new_denominator):
                target.append(Fraction(numerator,denominator))


product = 1
for frac in target:
    product *= frac

print(product.denominator)