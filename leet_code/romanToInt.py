def romanToInt(s):
    total = 0

    roman = {'I':1, 'V':5, 'X':10,
             'L':50, 'C':100, 'D':500, 'M':1000}
    
    s = s.replace('IV', 'IIII').replace('IX','VIIII')
    s = s.replace('XL', 'XXXX').replace('XC','LXXXX')
    s = s.replace('CD', 'CCCC').replace('CM','DCCCC')
    s = [i for i in s]
    for i in s:
        total += roman[i]
    return total

print(romanToInt('MCMXCIV'))
print(romanToInt('III'))