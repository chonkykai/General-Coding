def getSubstringCount(s):
    count = 0
    for i in s:
        if '10' in s:
            count+=1
        elif '01' in s:
            count+=1
    return count



print(getSubstringCount('0011'))