#! python3
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def isDevisable(num):
    if num % 20 == 0 and num % 19 == 0 and num % 17 == 0 and num % 16 == 0 \
        and num % 13 == 0 and num % 11 == 0 and num % 9 == 0 and num % 8 == 0 \
        and num % 7 == 0 and num % 4 == 0 and num % 3 == 0:
        return True

i = 2520
while not isDevisable(i):
    i += 20
print(i)

