import math

oddities_list = []

number_inputs = input("")
number_inputs = int(number_inputs)


for i in range (number_inputs):
    number_checking = input("")
    number_checking = int(number_checking)
    oddities_list.append(number_checking)

for i in range (number_inputs):
    if (oddities_list[i] % 2) == 0:
        print(f"{oddities_list[i]} is even")
    else:
        print(f"{oddities_list[i]} is odd")