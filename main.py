"""
primitve data
integer,
float,
complex (e.g: 1 + 2j)
"""

#string
name = "perseus evans"
print(name)
#there is 3 method to call string like concatenate
#1. Formatted string
print(f"hello guys, my name {name}\n")
#2. %-Formatting
print("my name %s \n" %name)
#3. str.format
print("my name is {} \n".format(name))


#data collection

#list
#list like an array in other language
name2 = 'liza'
my_list = [1, "january", 1.2]
print(my_list)
print(name2 + " " + my_list[1])

#dictionary
x = {'name' : 'andi', 'age' : 30, 'gender' : 'male'}
print(x)#print value of x
print(x['name']) #print value of key name 
#how to change value of key name
x['name'] ='george'
print(x)
print(x['name'])