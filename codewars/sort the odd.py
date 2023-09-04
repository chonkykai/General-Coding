def sort_array(source_array):
    odd_lst = []
    output = []
    if source_array == []:
        return []
    else: 
        for i in range (len(source_array)):
            if (source_array[i]%2 == 1):
                odd_lst.append(source_array[i])
        odd_lst.sort()
        x= 0
        for i in range(len(source_array)):
            if (source_array[i] %2) ==1:
                if len(odd_lst) >= x:
                    output.append(odd_lst[x])
                    x+=1
            else:
                output.append(source_array[i])
        return output