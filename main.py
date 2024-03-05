#create a class
class Car:
 #class without method
 #Attribute
 color = "Red"

#define object
#make a variable to have trait same as Car
car_1 = Car()

#to access attribute in Car class
print(car_1.color)

car_1.color = "Yellow"
print(car_1.color)


#class constructor
class MotorCycle:
 def __init__(self):
  self.color = "Blue"

myMotor = MotorCycle()

print(f"{myMotor.color}\n==========")

#with parameter
class SportCar:
 def __init__(self, color, brand, type):
  self.color = color
  self.brand = brand
  self.type = type

myCar_1 = SportCar("red","BMW","Electric Vehicle")

print(myCar_1.color)
print(myCar_1.brand)
print(f"{myCar_1.type}\n==========")

 