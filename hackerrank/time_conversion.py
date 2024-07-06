import math

def timeConversion(s):
    day = s[-2:]
    time = s[:8]
    time = time.split(':')
    convert = list(map(lambda x:int(x), time))
    if day == 'PM':
        if convert[0] == 12:
            pass
        else:
            convert[0] = convert[0] + 12
    else:
        if convert[0] == 12:
            convert[0] = convert[0] - 12
        else:
            pass

    str_convert = list(map(lambda x:str(x).zfill(2), convert))
    return ':'.join(str_convert)
    
    # print(day)
    # print(time)
    # print(convert)
    # print(':'.join(str_convert))


print(timeConversion('12:11:00AM'))
# print(timeConversion('08:01:00AM'))
# print(timeConversion('03:01:00PM'))