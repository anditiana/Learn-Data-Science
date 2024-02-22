#Looping

var_list = [1,2,3,4,5,6,7,8,9,10]
var_char = ['A','B','C','D','E']
for i in var_list:
 print(i)

print("\n")
for i in var_char :
 print(i)

print('\n')
#for in range
#range(start, stop, step)
#default range(stop) or range(star,stop)
#stop not include
for i in range(1, 20, 2):
 print(i)

print("==============")
#======================================
#while

counter = 1
while counter <= 5:
 print(counter)
 counter += 1


#for else
number = [1,2,3,4,5]
for num in number :
 if num == 9:
  print(f"w get {num}")
  break
else :
 print('number not found')

#if num has 3, program will execute w get 3, and then looping stop, else print number not found
print("==============")

#list comprehension 
num1 = [1, 2, 3, 4]
sq = []
for n in num1:
  sq.append(n**2)
print(sq)
#this is old 
#we can use this : new_;ist = [expression, for loop]
#in this example expression is n**2
print("new style")
num2 = [1, 2, 3, 4]
sq2 = [n**2 for n in num2]
print(sq2)