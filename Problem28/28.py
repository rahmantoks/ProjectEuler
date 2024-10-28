# Number Spiral Diagonals
# Starting with number 1 and moving to the right in the clockwise direction a 5 by 5 spiral is formed.
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Initialize variables

spiral_size = 1001  # Size of the spiral

total_sum = 1       # Start with the center of the spiral, which is 1



# Iterate over odd-sized spirals, starting from 3 to the given spiral size

for n in range(3, spiral_size + 1, 2):

    # The four diagonal numbers for each layer

    top_right = n**2

    top_left = top_right - (n - 1)

    bottom_left = top_left - (n - 1)

    bottom_right = bottom_left - (n - 1)

    

    # Add the diagonal numbers to the total sum

    total_sum += top_right + top_left + bottom_left + bottom_right



print(total_sum)  # This is the sum of the diagonal numbers for a 1001x1001 spiral