def narcissistic( value ):
    new_v = value
    count = str(value)
    length = len(count)
    ls = []
    for i in range(length):
        split_num = new_v%10
        new_v = new_v //10
        ls.append(split_num)
    for i in range (length):
        ls[i] = ls[i]**length
    sum_all = sum(ls)
    if value == sum_all:
        return True
    else: return False