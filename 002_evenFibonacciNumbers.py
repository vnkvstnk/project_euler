#! python3
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

summ = 2
number = 2
i = 1
while number < 4000000:
    number = number + i
    if number % 2 == 0:
        summ += number
    i = number - i

print(summ)
