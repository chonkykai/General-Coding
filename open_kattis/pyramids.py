import math

lst = []
height = 1
total = 0
blocks = int(input(""))

while total <=blocks:
    number = height*height
    if number > blocks:
        break
    else: 
        lst.append(number)
        height = height+2
        total = sum(lst)
        if total > blocks:
            final_lst = lst.pop()
            break
print(len(lst))
