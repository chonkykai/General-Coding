from math import sqrt

def find_next_square(sq):
    square = int(sqrt(sq))
    sq_1 = square*square
    if (sq_1 == sq):
        new = (square + 1) * (square + 1)
        return new
    else:
        return -1