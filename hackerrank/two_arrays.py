def twoArrays(k, A, B):
    sort_a = sorted(A)
    sort_b = sorted(B)[::-1]
    count = 0
    for i in range(len(A)):
        if sort_a[i] + sort_b[i] >= k:
            count += 1
        else:
            pass
    if count >= len(A):
        return 'YES'
    else:
        return 'NO'



print(twoArrays(10, [2, 1, 3], [7, 8, 9]))
print(twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4]))