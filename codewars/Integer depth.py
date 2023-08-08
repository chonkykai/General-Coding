def compute_depth(n):
    ls = []
    ls2 = [0,1,2,3,4,5,6,7,8,9]
    i = 1
    while True:
        multi = n*i
        new = str(multi)
        for x in range (len(new)):
            ls.append(int(new[x]))
        output = list(dict.fromkeys(ls))
        check = all(item in ls for item in ls2)
        if check is True:
            return i
            break
        else: 
            i +=1