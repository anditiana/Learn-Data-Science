#Day-5-Array Challenge
'''
there is an array from 0 to 101
calculate the average value of array
store the value in result
'''

var_array = [i for i in range(0,101)]

temp_value = 0
for i in range(len(var_array)):
 temp_value += var_array[i]

result = temp_value/len(var_array)

print(result)