def expanded_form(num):
    x = 10
    lst = []
    while num != 0:
        if num%x != 0:
            lst.append(str(num%x))
            num = num - num%x
            x = x*10
        else:
            x = x*10
        
    lst.reverse()
    return ' + '.join(lst)


print(expanded_form(12))

print(expanded_form(70304))