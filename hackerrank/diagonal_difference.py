def diagonalDifference(arr):
    cross1 = 0
    cross2 = 0
    for i in range (len(arr)):
        # print(arr[i])
        for x in range (len(arr[i])): # cross
            if i == x:
                cross1 = cross1 + arr[i][x]
                arr[i] = arr[i][::-1]
                cross2 = cross2 + arr[i][x]
    
    return abs(cross1 - cross2)
    # print(arr[0])



print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))