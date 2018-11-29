# Project Euler, problem #17
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many letters would be used?
from num2words import num2words

count = 0
to_remove = ' -'
table = str.maketrans(dict.fromkeys(to_remove))
for i in range(1, 1001):
    count += len(num2words(i).translate(table))
print(count)