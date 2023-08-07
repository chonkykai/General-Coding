def high_and_low(numbers):
    numbers = numbers.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    
    return str(max(numbers)) + " " + str(min(numbers))