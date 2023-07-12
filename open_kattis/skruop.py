base = 7
volume = int(input(""))

for i in range (volume):
    request = input("")
    if base == 0:
        if request == "Skru op!":
            base += 1
        else:
            continue
    elif base == 10:
        if request == "Skru ned!":
            base -= 1
        else:
            continue
    elif (base!= 0 or base != 10): 
        if request == "Skru op!":
            base += 1
        elif request == "Skru ned!":
            base -= 1

print(base)
