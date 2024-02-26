#error handling

#try except
#e.g simple error handling
z = 0
try : 
 print(1/z)
except ZeroDivisionError:
 print("You can't divide by 0")


#the comple error handling

p = 2
try:
 result = 10 / 0
except ZeroDivisionError:
 print("You can't divide by 0")
else:
 print("Result:", result)
finally:
 print("Finish.")

#error handling with more than one except

var_dict = {"average" : "1.0"}

try : 
 print(f"average {var_dict['average']}")
except KeyError :
 print("Key not found")
except TypeError:
 print("you can't divide number with string")
else:
 print("Your code is work")
finally:
 print("End of program")
 
#Raise
var = -1

if var < 0:
 raise ValueError("negative number is forbidden")
else:
 for i in range(var):
     print(i+1)
  
