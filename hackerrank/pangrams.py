def pangrams(s):
    lst = s.split(' ')
    mini_lst = []
    for i in lst:
        i = i.lower()
        for x in range (len(i)):
            mini_lst.append(i[x])
    mylst = list(dict.fromkeys(mini_lst))
    if len(mylst) == 26:
        return 'pangram'
    else:
        return 'not pangram'

print(pangrams('We promptly judged antique ivory buckles for the next prize'))
print(pangrams('We promptly judged antique ivory buckles for the prize'))
