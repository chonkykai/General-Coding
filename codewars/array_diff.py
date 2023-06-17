def array_diff(a, b):
    c = a.copy()
    if b != []:
        for x in range (len(b)):
            for y in range (len(a)):
                if b[x] not in c:
                    continue
                if (b[x] - a[y]) == 0:
                    c.remove(b[x])
                else:
                    continue
        return c
    else:
        return a