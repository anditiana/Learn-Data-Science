#inheritance quiz
"""
 1. make a class name Animal with following conditions:
    #have a properties :
     - name
     - age
     - species
    # have constructor :
     - name
     - age
     - species

 2. make a class name Cat
    # Cat is child class from Animal
    # have method : 
     - description 
        will return : "{self.name} is cat with {self.species} species, age {self.age} years old"
     - sound 
        will return "meow!"

 3. make instance from Cat named "myCat" with following :
     - name = Neko
     - age = 3
     - species = Persian
"""


class Animal:
 def __init__(self, name, age, species):
  self.name = name
  self.age = age
  self.species = species


class Cat(Animal):
 def description(self):
  return f"{self.name} is cat with {self.species} species, age {self.age} years old"

 def sound(self):
  return "meow!"


myCat = Cat("Neko", 3, "Persian")

