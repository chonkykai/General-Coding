def positive_sum(arr):
    arr_2 = []
    for i in range (len(arr)):
        if (arr[i] >0):
            arr_2.append(arr[i])
    if (arr_2 == []):
        return 0
    else:
        sum_arr = sum(arr_2)
        if (sum_arr < 0):
            return 0
        return sum_arr