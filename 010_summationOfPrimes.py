#! python3
# Project Euler, problem #10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from time import time
start = time()
potentialPrimes = list(range(2, 2000001))
primes = []

for i in range(len(potentialPrimes)):
    if potentialPrimes[i] == '0':
        continue
    primes.append(potentialPrimes[i])
    potentialPrimes[i + potentialPrimes[i]::potentialPrimes[i]] = '0' * len(potentialPrimes[i + potentialPrimes[i]::potentialPrimes[i]])
print(sum(primes))
print(len(primes))
print('It took %s seconds' % (time() - start))
