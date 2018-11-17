#! python3
# What is the largest prime factor of the number 600851475143 ?
import math

number = 600851475143


# define if a number is a factor ov the given number
def getFactors(aNumber):
    factors = []
    for potentialFactor in range(1, int(math.sqrt(aNumber)) + 1):
        if aNumber % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(aNumber // potentialFactor)
    return factors


# define if a factor is prime
def isPrime(factor):
    return len(getFactors(factor)) == 2     # factor is prime if it has only two factors (1 and itself)

# find the largest prime factor
allFactors = getFactors(number)
maxPrimeFactor = 0
for i in range(1, len(allFactors)):
    if isPrime(allFactors[i]) and allFactors[i] > maxPrimeFactor:
        maxPrimeFactor = allFactors[i]

print('The maximum prime factor for number %s is %s' % (number, maxPrimeFactor))
