def matchingStrings(strings, queries):
    count = []
    
    for i in queries:
        sum = 0
        for x in strings:
            if i == x:
                sum += 1
            else: pass
        count.append(sum)
    return count

    

# print(matchingStrings(['def','de','fgh'], ['de','lmn','fgh']))
# print(matchingStrings(['abcde','sdaklfj','asdjf','na','basdn','sdaklfj','na','asdjf','na','basdn','sdaklfj','asdjf'],
#                        ['abcde','sdaklfj','asdjf','na','basdn']))
print(matchingStrings(['aba','baba','aba','xzxb'], ['aba','xzxb','ab']))