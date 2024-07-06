def seq(n):
    ls = [0]
    for i in range(n-1):
        last_item = ls[-1] #get latest number
        if last_item in ls[:-1]:
            ind = [i for i, x in enumerate(ls) if x == last_item]
            pos1 = max(ind)
            ind.pop()
            pos2 = max(ind)
            dist = pos1 - pos2
            ls.append(dist)
        else:
            ls.append(0)
    output = ls[n-1]
    return output