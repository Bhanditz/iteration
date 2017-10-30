# Iteration Pattern
# Doing the same thing once for each member of a list.

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
    # standard for loop with range
    # for i in range(0, len(list)):
    # 	print list[i]

    # for each loop
    for item in list:
        print item

def print_scores(names, scores):
    for i in range(0, len(names)):
        print names[i] , " scored " , scores[i]

# filter pattern
def congratulations(names, scores):
    for i in range(0, len(names)):
        if (scores[i] == 100):
            print "Congrats", names[i], "! You got a perfect score!"

def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    
    return total

def max(numbers):
    current_max = numbers[0]
    for n in numbers:
        if n > current_max:
            current_max = n
    
    return current_max

# Find the sum but substitute subtraction for every other addition
def alternating_sum(numbers):
    add = True
    total = 0
    for n in numbers:
        if add:
            total += n
            add = False
        else:
            total -= n
            add = True
    return total

# Pass the function ints and a min and max, find the sum of all numbers not in this range
def sum_outside(numbers, min, max):
    total = 0
    for n in numbers:
        if n < min:
            total += n
        elif n >= max:
            total += n
    return total

# Pass the function ints and a divisor, count how many numbers are 1 off from being divisible
def count_close_remainders(numbers, divisor):
    total = 0
    for n in numbers:
            if n % divisor == 1 or n % divisor == divisor - 1 or n % divisor == 0:
                total += 1
    return total

# Pass the function ints and a target, return the list with numbers doubled if they are smaller than the previous number or within 3 of the target
def double_down(numbers, target):
    final = []
    for n in range(len(numbers)):
        if n == 0:
            if numbers[n] - target > -3 and numbers[n] - target < 3:
                final.append(numbers[n] * 2)
            else:
                final.append(numbers[n])
        else:
            if numbers[n] < numbers[n-1] or numbers[n] - target > -3 and numbers[n] - target < 3:
                final.append(numbers[n] * 2)
            else:
                final.append(numbers[n])
    return final

