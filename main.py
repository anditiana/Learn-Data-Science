#Function
#build function

def rectangle_area(length, width):
 rec_area = length * width
 return rec_area

#call function
result = rectangle_area(3,5)
print(f"{result} \n================")


#keyword argumen
#we call keyword argumen when we define parameter with value
#f(x=a) = 2x

result2 = rectangle_area(length=4, width= 4)
print(f"{result2}\n================")


#parameter

#1. parameter positional only
# def function_name(param1, param2, /)

def triangle_area(a,b,/):
 return (a*b)/2

print(f"triangle area : {triangle_area(3,4)}\n================")
#but if we define the parameter while call function it cause error
# e.g : triangle_area(a=3, b=4) ===> it cause error


#2. parameter keyword only
#when call function parameter value must define
def greeting(*, name, message):
 print(f"Hello {name}, {message}\n================")

#parameter has value 
greeting(name="lirio", message="good moorning")

#not define value in parameter causing error
#e.g greeting(name, message)