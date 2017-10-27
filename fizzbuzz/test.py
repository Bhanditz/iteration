from fizzbuzz import *
from random import randint

numbers = [354,281,946,290,333,30,66,41]

random_numbers = []
for i in range(0, 99):
    random_numbers.append(randint(0,999))

print fizzbuzz(numbers)
print
print
print fizzbuzz(random_numbers)