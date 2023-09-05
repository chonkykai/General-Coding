import math

def square_sum(numbers):
    for i in range (len(numbers)):
        numbers[i] = pow(numbers[i],2)
    return sum(numbers)