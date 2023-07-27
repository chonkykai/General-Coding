def digital_root(n):
    n2 = str(n)
    x = n
    while True:
        total = 0
        if x < 9:
            return x
        elif n > 9:
            for i in range (len(n2)):
                total += n%10
                n = n//10
            if total > 9:
                n = total
            else:
                break
        else:
            break
    return total