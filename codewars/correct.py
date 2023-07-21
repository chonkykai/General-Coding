def correct(s):
    ls = []
    for i in range(len(s)):
        ls.append(s[i])
    for i in range(len(ls)):
        if ls[i] == '0':
            ls[i] = 'O'
        if ls[i] == '5':
            ls[i] = 'S'
        if ls[i] == "1":
            ls[i] = 'I'
    output = ''.join(ls)
    return output