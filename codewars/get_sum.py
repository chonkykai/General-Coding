def get_sum(a,b):
    count = abs(b - a)
    lst = []
    if a > b:
        initial = b
    else:
        initial = a
    for i in range (count+1):
        lst.append(initial)
        initial += 1
    total = sum(lst)
    return total