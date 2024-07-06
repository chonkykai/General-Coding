def is_valid_walk(walk):
    n,s,w,e = 0,0,0,0
    if len(walk) < 10:
        return False
    elif len(walk) > 10:
        return False
    else:
        for i in range (len(walk)):
            if walk[i] == 'n':
                n += 1
            elif walk[i] == 's':
                s += 1
            elif walk[i] == 'w':
                w += 1
            elif walk[i] == 'e':
                e += 1
        if (n == s) & (w == e):
            return True
        else:
            return False