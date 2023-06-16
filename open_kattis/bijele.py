import math
chess = (1, 1, 2, 2, 2, 8)
chess_input = input("")
chess_input = chess_input.split(" ")
for i in range (6):
    chess_input[i] = int(chess_input[i])
for i in range (6):
    print(chess[i] - chess_input[i], end=" ")