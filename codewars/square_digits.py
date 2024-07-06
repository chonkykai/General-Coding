def square_digits(num):
    lst = []
    for i in range(len(str(num))):
        lst.append((num%10)**2)
        num = num//10
    return int(''.join(map(str,lst[::-1])))



print(square_digits(765))