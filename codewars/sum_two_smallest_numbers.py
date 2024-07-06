def sum_two_smallest_numbers(numbers):
    small = []
    small.append(min(numbers))
    numbers.remove(min(numbers))
    small.append(min(numbers))
    return sum(small)