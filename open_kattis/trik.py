jumble_lst = []
ball = ["1","0","0"]

jumble = input("")
for i in range (len(jumble)):
    jumble_lst.append(jumble[i])

for i in range(len(jumble_lst)):
    if jumble_lst[i] == "A":
        # sequence A
        ball += [ball.pop(0)]
        ball += [ball.pop(0)]
        ball += [ball.pop(1)]
        ball += [ball.pop(0)]
    elif jumble_lst[i] == "B":
        # sequence B
        ball += [ball.pop(1)]
    elif jumble_lst[i] == "C":
        # sequence C
        ball += [ball.pop(1)]
        ball += [ball.pop(0)]

index = ball.index("1")
if index == 0:
    print("1")
elif index == 1:
    print("2")
else:
    print("3")