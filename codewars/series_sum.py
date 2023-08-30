def series_sum(n):
    x = 4
    total = 1
    if n == 0:
        return '0.00'
    else:

        for i in range (n-1):
            total += 1/x
            x += 3
        result = str(f'{total:.2f}')
        return result