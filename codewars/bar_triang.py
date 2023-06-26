import math

def bar_triang(p1, p2, p3): 
    x_origin = (p1[0] + p2[0] + p3[0])/3
    x_origin = float("{0:.4f}".format(x_origin))
    y_origin = (p1[1] + p2[1] + p3[1])/3
    y_origin = float("{0:.4f}".format(y_origin))
    lst = [x_origin, y_origin]
    return lst