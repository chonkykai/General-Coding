import math
import os
import random
import re
import sys

def weird (n):
    if (n >=2 and n <= 5) and (n%2 == 0):
        print('Not Weird')
    elif (n >=6 and n <= 20) and (n%2 == 0):
        print('Weird')
    elif (n >=20) and (n%2 == 0):
        print('Not Weird')
    else:
        print ('Weird')

print(weird(3))
print(weird(16))