#! python3
# What is the 10 001st prime number?
import math
import logging
logging.basicConfig(level='DEBUG')

potentialPrimes = list(range(2, 2000000))
primes = []
i = 0
while len(primes) < 1001:
    if str(potentialPrimes[i]) == '0':
        i += 1
        continue
    primes.append(potentialPrimes[i])
    # should find a way to replace all the elements at once
    potentialPrimes[i + potentialPrimes[i]::potentialPrimes[i]] = '0' * len(potentialPrimes[i + potentialPrimes[i]::potentialPrimes[i]])
    i += 1

print(primes[-1])
