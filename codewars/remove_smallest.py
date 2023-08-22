def remove_smallest(numbers):
    new = numbers.copy()
    print(new)
    if new != []:
        minimum = min(new)
        new.remove(minimum)
        return new
    else:
        return numbers