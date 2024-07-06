def miniMaxSum(arr):
    arr.sort()
    # find min sum of 4 integers and max sum of 4 integers in arr
    max_sum = arr[1:]
    min_sum = arr[:4]

    print(sum(min_sum), sum(max_sum))
print(miniMaxSum([1,2,3,4,5]))