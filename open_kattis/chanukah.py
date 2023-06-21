import math

holiday = []
holiday_2 = []
no_input = int(input(""))

for i in range (no_input):
    event_input = input("")
    holiday.append(event_input.split(" "))

for x in range (no_input):
    for y in range (0,1):
        holiday_2.append(holiday[x][1])

for i in range (len(holiday_2)):
    holiday_2[i] = int(holiday_2[i])

for i in range (len(holiday_2)):
    summation = 0
    for x in range (holiday_2[i]+1):
        summation = summation + x
    summation = summation + holiday_2[i]
    print(f"{i+1} {summation}")