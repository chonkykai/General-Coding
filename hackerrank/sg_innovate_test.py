def smallestNegativeBalance(debts):
    num_debts = debts
    num_value = input('Enter number: ') # always 3
    lst = []
    for i in range (debts):
        record = input('enter input: ')
        lst.append(record)
    table = {}
    for i in lst:
        row = i.split(' ')
        table[row[0]] = 0
        table[row[1]] = 0
    for i in lst:
        value = i.split(' ')
        
        if (table[value[0]] != 0) or (table[value[0]] == 0):
            table[value[0]] = table.get(value[0]) + int(value[2])

        elif (table[value[1]] != 0) or (table[value[1]] != 0):
            table[value[1]] = table.get(value[1]) + -int(value[2])
        else:
            table.update({value[0]:int(value[2]),value[1]:-int(value[2])})
    smallest = min(table, key=table.get)
    if table.get(smallest) > 0:
        return 'Nobody has a negative balance'
    else:
        return smallest



print(smallestNegativeBalance(2))
# int(row[2])