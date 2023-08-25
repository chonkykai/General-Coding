def rgb(r, g, b):
    # create a dictionary
    convert = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4',
               5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
               10:'A', 11:'B', 12:'C', 13:'D', 14:'E',
               15:'F'}
    colors = [r, g, b]
    lst = []
    for i in range (len(colors)):
        if (colors[i] > 0):
            if colors[i] >255:
                lst.append('FF')
            else:
                quotient = colors[i]//16
                remainder = colors[i]%16
                lst.append(str(convert[quotient]))
                lst.append(str(convert[remainder]))
        else:
            lst.append('00')
    
    print(''.join(lst))

# ========================
rgb(0, 0, 0)
rgb(1, 2, 3)
rgb(255, 255, 255)
rgb(254, 253, 252)
rgb(-20, 275, 125)