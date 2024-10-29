# Pandigital Products
# We shall say that n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234 is 1 through 5 pandigital
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing, multiplicant, multiplier, and product is 1 to 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

def ispandigital(str):
    return len(str) == 9 and set(str) == set("123456789")

def find_product_sum():
    products = set()

    for multiplicand in range(1,100):
        for multiplier in range(1,2000):
            product = multiplier * multiplicand

            combined = f"{multiplicand}{multiplier}{product}"

            if len(combined) > 9:
                break

            if ispandigital(combined):
                products.add(product)

    return sum(products)


print(find_product_sum())