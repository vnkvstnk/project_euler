#! python3
# Project Euler, problem #12
# What is the value of the first triangle number to have over five hundred divisors?

# how the program should work:
# 1. Iterate through a list of triangular numbers (n * (n + 1)) / 2
# 2. Find all the prime numbers below the trNumber / 2 (trNumber - triangular number)
# 3. Factorize the trNumber starting from the largest prime found
# 4. Calculate the number of divisors
import logging
logging.basicConfig(level='DEBUG')
logging.disable()
divisorsDatabase = []
numOfDivisors = 0
n = 2000                   # n in (n * (n + 1)) / 2 - calculates next trNumber
# for n in range(1, 1001):
while numOfDivisors <= 500: # uncomment when an appropriate algorithm is found
    trNumber = int((n * (n + 1)) / 2)    # calculates a prime number
    answer = trNumber       # saving the number to display later
    # 2. Find all the prime numbers below the trNumber / 2
    potentialPrimes = list(range(2, int(trNumber / 2)))
    primes = []         # list of primes below trNumber / 2
    for i in range(len(potentialPrimes) - 1):
        if str(potentialPrimes[i]) == '0':
            continue
        primes.append(potentialPrimes[i])
        potentialPrimes[i + potentialPrimes[i]::potentialPrimes[i]] = '0' * len(potentialPrimes[i + potentialPrimes[i]::potentialPrimes[i]])
    # 3. Factorize the trNumber starting from the largest prime found
    factors = []
    for prime in primes:
        while trNumber % prime == 0:
            factors.append(prime)
            trNumber = trNumber / prime
            if trNumber == 1:
                break
    # 4. Calculate the number of divisors
    # The number of divisors is calculated as described here:
    # https://math.stackexchange.com/questions/433848/prime-factors-number-of-divisors
    # 4.1 First count occurrences of each factor in a list
    counts = []
    for factor in factors:
        if factor == 0:
            continue
        counts.append(factors.count(factor))
        factors = [x for x in factors if x != factor]
    counts = [x for x in counts if x != 0]
    # 4.2 Calculate the number of divisors
    numOfDivisors = 1
    for count in counts:
        numOfDivisors = numOfDivisors * (count + 1)

    divisorsDatabase.append(numOfDivisors)
    logging.debug(divisorsDatabase)

    n += 1


output = open('output.txt', 'w')
output.write('[')
for i in divisorsDatabase:
    output.write(str(i) + ', ')
output.write(']')
output.close()








