def unique_in_order(iterable):
    if iterable == '':
        return []
    else:
        lst = [iterable[0]]
        x = 0
        for i in range (len(iterable)):
            if lst[x] != iterable[i]:
                lst.append(iterable[i])
                x +=1
            else:
                continue
        return (lst)