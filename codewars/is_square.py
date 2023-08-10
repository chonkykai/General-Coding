def is_square(n):
    if n == 0: return True
    if n <0: return False
    elif abs(n)%(abs(n)**0.5) == 0: return True
    else: return False





print(is_square(-1))