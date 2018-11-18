# Project Euler, problem #21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
# Evaluate the sum of all the amicable numbers under 10000.

def divisors_sum(number):
    divisors = []
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)


def amicable_sum(number):
    amicables = set()
    for i in range(number):
        j = divisors_sum(i)
        if divisors_sum(j) == i and i != j and j < number:
            amicables.add(i)
            amicables.add(j)
    return sum(amicables)


print(amicable_sum(10000))
# Done!
