# Project Euler, problem #25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def nth_fib(number):
    if number in (1, 2):
        return 1
    counter = 3
    fib_i = 1
    fib_j = 1
    while counter != number + 1:
        fib_i, fib_j = fib_j, fib_i + fib_j
        counter += 1
    return fib_j

n_digits = 0
i = 4000
while n_digits < 1000:
    n_digits = len(str(nth_fib(i)))
    i += 1
print(i - 1)
