import math

lst = []

at_bats = int(input(""))
actions = input("")
actions = actions.split(" ")

for i in range (len(actions)):
    actions[i] = int(actions[i])

for i in range (at_bats):
    if actions[i] != -1:
        lst.append(actions[i])

output = sum(lst)/len(lst)
print(output)