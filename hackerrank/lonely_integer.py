def lonelyinteger(a):
    main_lst = a.copy()
    for i in a:
        count = 0
        for x in main_lst:
            if x == i:
                count += 1
        if count == 1:
            return i



print(lonelyinteger([1,2,3,4,3,2,1]))