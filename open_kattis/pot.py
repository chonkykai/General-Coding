import math

newlist = []
finalist = []

number_values = input("")
number_values = int(number_values)

for number_values in range(number_values):
    integer_values = input("")
    integer_values = int(integer_values)
    newlist.append(integer_values)

for i in range(len(newlist)):
    power = newlist[i]%10
    quotient = newlist[i]//10
    finalist.append(pow(quotient, power))

print(sum(finalist))