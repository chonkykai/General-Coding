lst = ['empty']
blimp = False

output = []
for i in range (5):
    message = input("")
    lst.append(message)

for i in range (1,6):
     if "FBI" in lst[i]:
        print(i, end = " ")
        blimp = True
if blimp == False:
    print("HE GOT AWAY!")
