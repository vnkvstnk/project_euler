#! python3
# Project Euler, problem #9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for m in range(40):
    for n in range(40):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n**2
        if a + b + c == 1000:
            print('a = %s\nb = %s\nc = %s\nProduct = %s' % (a, b ,c, a * b * c))
