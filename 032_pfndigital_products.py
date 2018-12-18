# Project Euler, problem #32
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

def is_pandigital(number):
    if len(number) > 9:
        return False
    numbers = '123456789'
    number = sorted(list(number))
    number = ''.join(number)
    if number == numbers:
        return True
    return False

sum_ = set()
for i in range(1, 100):
    for j in range(i, 8000):
        m = i * j;
        s = str(m) + str(i) + str(j)
        if is_pandigital(s):
            sum_.add(m)
