#! python3
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

# A brute force solution

# import logging
# logging.basicConfig(level='DEBUG')
# sumOfSquares = 0
# sum = 0
# for i in range(1, 101):
#     sumOfSquares += i ** 2
#     sum += i
# squaredSum = sum ** 2
# difference = squaredSum - sumOfSquares
# print(difference)

# A clever solution

limit = 100
sum = limit * (limit + 1) / 2
sumOfSquares = limit * (limit + 1) * (2 * limit + 1) / 6
print(sum ** 2 - sumOfSquares)



