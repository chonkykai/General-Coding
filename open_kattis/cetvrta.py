import math

lst = []
x_value = []
y_value = []

for i in range (3):
    num_in = input("")
    lst.append(num_in.split(" "))

for x in range (3):
    for y in range (2):
        lst[x][y] = int(lst[x][y])

for x in range(3):
    for y in range (2):
        if (y%2) == 0:
            x_value.append(lst[x][y])
        else:
            y_value.append(lst[x][y])

if x_value.count(min(x_value)) == 1:
    countx = min(x_value)
else:
    countx = max(x_value)

if y_value.count(min(y_value)) == 1:
    county = min(y_value)
else:
    county = max(y_value)

print(f'{countx} {county} ')