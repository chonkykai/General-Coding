import math

num_list = []
processing_num = 0
num_input = input("")
num_input = int(num_input)

sum_input = input("")
sum_input = sum_input.split(" ")

for i in range(num_input):
    processing_num = int(sum_input[i])
    num_list.append(processing_num)

print(sum(num_list))