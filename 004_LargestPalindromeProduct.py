import logging
from timeit import default_timer as timer
logging.basicConfig(level='DEBUG')
logging.disable()
# function to check if number is palindrome
def isPalindrome(num):
    initNum = num       # saving the initial number
    reverse = 0
    while num > 0:
        lastDigit = num % 10
        reverse = (reverse * 10) + lastDigit
        num = num // 10
    return reverse == initNum
logging.debug(isPalindrome(121))

start = timer()
# looking for palindromes in products of numbers between 900 and 999
palindromes = []
multipliers = range(900, 1000)
for i in range(0, len(multipliers)):
    for j in range(i, len(multipliers)):
        potentialPalindrome = multipliers[i] * multipliers [j]
        if isPalindrome(potentialPalindrome):
            palindromes.append(potentialPalindrome)
logging.debug(palindromes)
end = timer()
print(palindromes)
print('The maximum palindrome is %s' % max(palindromes))
print('Ececution time - %s s' % (end - start))


