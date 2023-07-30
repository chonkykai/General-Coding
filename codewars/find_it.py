def find_it(seq):
    lst = []
    odd = []
    unique = list(set(seq))
    seq.sort()
    for i in unique:
        count = 0
        for x in seq:
            if i == x:
                count +=1
        lst.append(count)
    for y in lst:
        if y%2 !=0:
            odd.append(y)
    return unique[lst.index(max(odd))]



print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])) 