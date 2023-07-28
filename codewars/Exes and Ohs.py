def xo(s):
    s = s.lower()
    x = []
    o = []
    for i in range (len(s)):
        if s[i] == "x":
            x.append(s[i])
        elif s[i] == "o":
            o.append(s[i])
    if (len(x) == (len(o))): return True
    elif (len(x) or len(o)) == 0: return True
    elif(bool(x) or bool(o)): return False
    else: return False