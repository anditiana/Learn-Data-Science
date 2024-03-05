#Inheritance
#Parent Class
class Car:
 def __init__(self, color, brand, speed):
  self.color = color
  self.brand = brand
  self.speed = speed

 def increase_speed(self):
  self.speed += 20

car_1 = Car("Black","BMW",150)
print("=========Basic Car===========")
print(f"Car speed : {car_1.speed} km/h")
car_1.increase_speed()
print(f"After Increase Speed : {car_1.speed} km/h")


#add child class

class SportCar(Car):
 def turbo(self):
  self.speed += 50

 """
 override
 add same method increase_speed as parent class but different action
 """
 def increase_speed(self):
  self.speed += 30

 """
 but if we want to use same method and attribute as parent class we can use 
 super() instead write it from scratch
 
 syntax : super().method_name_from_parent_class()

 def increase_speed(self):
  super().increase.speed()
 """
  
car_sport_1 = SportCar("Red", "Ferrari", 200)
print("=========Sport Car===========")
print(f"Normal Speed : {car_sport_1.speed} km/h")

#using method turbo
car_sport_1.turbo()
print(f"Turbo Speed : {car_sport_1.speed} km/h ")

car_sport_1.increase_speed()
print(f"After Increase Speed : {car_sport_1.speed}km/h \n=====================")


"""
 the result of car_sport_1.speed is 280, why not 230?
 because turbo method have called first that make current speed is 250
 then we call method increase_speed() that means we add current speed is 250 + 30 = 280 
"""
