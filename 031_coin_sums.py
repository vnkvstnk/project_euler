# Project Euler, problem #30
# How many different ways can £2 be made using any number of coins?
# (1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).)
from pprint import pprint as pp
global cases


def number_of_ways(n, coins):
    if n == 0:
        return 1
    sum_ = 0
    for coin in coins:
        if n - coin >= 0:
            if n - coin in cases:
                sum_ += cases[n - coin]
            else:
                a = number_of_ways(n - coin, coins)
                sum_ += a
                cases[n - coin] = a
    return sum_


coins = [1, 2, 5]
cases = dict()
total = [0,]
for n in range(1, 200 + 1):
    if n in cases.keys():
        total[n] = cases[n]
    else:
        total.append(number_of_ways(n, coins))
        cases[n] = total[n]
print(total)
pp(cases)