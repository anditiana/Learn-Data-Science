#array
'''
there is 2 method to use array,
first we can use list as array
or, we can add module array i.e from NumPy
'''


#array using list

var_array = [1,2,3,4,5,6]
length_arr = len(var_array)
print(f"Array = {var_array}")
print(f"Array length = {length_arr}")

#we can use list comperhension to set default value
var_arr = [0 for i in range(10)]
print(var_arr)

#and then we can set value 
for index in range(10):
 var_arr[index] = index + 1

print(f"New Array = {var_arr}")


#array exercise
#find a highest number in array
my_arr = [1,7,2,89,3]
left_pointer = my_arr[0]

for i in range(1, len(my_arr)):
 right_pointer = my_arr[i]
 if right_pointer > left_pointer:
  left_pointer = right_pointer

print(left_pointer)
  