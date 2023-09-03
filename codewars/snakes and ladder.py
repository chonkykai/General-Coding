def snakes_and_ladders(board, dice):
    artifact_pos = board[0]
    for i in range (len(dice)):
        rolled_dice = dice[i]
        move = rolled_dice + artifact_pos
        if move > len(board):
            move = move - artifact_pos
            continue
        elif move < len(board):
            if board[move] !=0:
                move = move + board[move]
                artifact_pos = move
            else: 
                artifact_pos = move
                continue
        elif move == len(board):
            continue
    return artifact_pos