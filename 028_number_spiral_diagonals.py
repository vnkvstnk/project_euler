# Project Euler, problem #28
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# The general formula for the sum is:
# (sum for n from 1 to N of 4 ** (2 * n + 1) ** 2 - 12 * n) + 1,
# where n is number of iteration (steps from the center, where iteration 1 is 3 by 3 square)
# and N is the maximum number of iterations

s = 1001  # matrix dimention
N = (s - 1) // 2  # maximum number of iterations
sum_ = 0
for n in range(1, N + 1):
    sum_ += 4 * (2 * n + 1) ** 2 - 12 * n
print(sum_ + 1)