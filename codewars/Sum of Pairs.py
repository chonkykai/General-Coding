def sum_pairs(ints, s):
    for i in range(len(ints)):
        for x in range(i, len(ints)):
            sum = ints[i] + ints[x]
            if sum == s: 
                print([ints[i],ints[x]])
                print([ints.index(ints[i]),ints.index(ints[x])])
            else: 
                pass



# sum_pairs([1, 4, 8, 7, 3, 15], 8)
sum_pairs([10, 5, 2, 3, 7, 5] , 10)


# x = ['a','v','s','d']
# print(x.index('s'))