def find_uniq(arr):
    num1 = arr[0]
    lst1 = []
    lst2 = []
    for i in range (len(arr)):
        if num1 == arr[i]:
            lst1.append(arr[i])
        else:
            lst2.append(arr[i])
    if len(lst1) > len(lst2):
        return (lst2[0])
    else:
        return (lst1[0])