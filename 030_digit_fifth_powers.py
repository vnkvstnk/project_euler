# Project Euler, problem #30
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def is_sum_of_digits(n, power):
    sub_sum = 0
    origal_number = n
    while n:
        last_digit = n % 10
        sub_sum += last_digit ** power
        n //= 10
    return origal_number == sub_sum


sum_ = 0
# 6 * 9 ** 5 is the limit above wich a number cannot be expressed as sum of its digits to the fifth
for i in range(2, 6 * 9 ** 5):
    if is_sum_of_digits(i, 5):
        sum_ += i
print(sum_)