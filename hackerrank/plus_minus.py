def plusMinus(arr):
    pos = 0
    neg = 0
    neu = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else: 
            neu += 1
    print("{:.6f}".format(pos/len(arr)))
    print("{:.6f}".format(neg/len(arr)))
    print("{:.6f}".format(neu/len(arr)))


print(plusMinus([-4, 3, -9, 0, 4, 1]))