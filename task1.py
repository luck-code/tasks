#!/usr/bin/python3
import sys
from itertools import cycle

length_array = int(sys.argv[1])  # 5
step = 1
steps = int(sys.argv[2])  # 4
array = [x+1 for x in range(length_array)]
temp_array = []
collection_temp_arrays = []
first_element = True

for number in cycle(array):
    if first_element:
        temp_array.append(number)
        first_element = False
    elif step < steps:
        temp_array.append(number)
        step += 1
        if step == steps:
            first_element = True
            step = 2
            collection_temp_arrays.append(temp_array)
            if temp_array[steps - 1] == array[0]:
                break

            temp_array = []
            temp_array.append(number)

result_array = []
for i in range(len(collection_temp_arrays)):
    result_array.append(collection_temp_arrays[i][0])


def list_to_int(result_array):
    string = ''
    for element in result_array:
        string += str(element)
        # return int(string)
    print(int(string))


list_to_int(result_array)
