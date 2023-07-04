import math

advertistments = []

num_values = int(input(""))

for i in range (num_values):
    inputs_adv = input("")
    advertistments.append(inputs_adv.split(" "))

for x in range (num_values):
    for y in range (0,3):
        advertistments[x][y] = int(advertistments[x][y])

for x in range (num_values):
    cost = advertistments[x][1]-advertistments[x][2]
    if cost > advertistments[x][0]:
        print("advertise")
    elif cost < advertistments[x][0]:
        print("do not advertise")
    else:
        print("does not matter")
