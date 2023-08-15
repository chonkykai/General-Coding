def move_zeros(lst):
    for i in range (len(lst)):
        if lst[i] == 0:
            lst.append(lst.pop(lst.index(0)))
        else:
            continue
    return lst 