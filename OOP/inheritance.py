# class Animal:
#   def __init__(self,name,is_alive):
#     self.name=name
#     self.is_alive=is_alive

#   def sleep(self):
#     print("This animal is asleep")

#   def eat(self):
#     print("This animal is asleep")
  
# class Dog(Animal):
#   # def __init__(self,name,is_alive,colour):
#   #   super().__init__(self,name,is_alive)
#   #   self.colour=colour

#   def Talk(self):
#     print(f"{self.name} is Barking.")
  
# class Cat(Animal):
#   # def __init__(self,name,is_alive,colour):
#   #   super().__init__(self,name,is_alive)
#   #   self.colour=colour

#   def Talk(self):
#     print(f"{self.name} is purring.")
  
# class Mouse(Animal):
#   # def __init__(self,name,is_alive,colour):
#   #   super().__init__(self,name,is_alive)
#   #   self.colour=colour

#   def Talk(self):
#     print(f"{self.name} is squeeking.")

# mouse=Mouse("Mickey",True)
# dog=Dog("Max",True)
# cat=Cat("Tom",True)

# mouse.Talk()


# MULTIPLE AND MULTILEVEL INHERITANCE

# Multiple inheritance => a class is inheriting from another class
# Multilevel inheritance => a class inherits from a class which inherits from another class 

# class Animal:
#   def __init__(self,name):
#     self.name=name

#   def eat(self):
#     print(f"{self.name} is eating.")

#   def sleep(self):
#     print(f"{self.name} is sleeping.")

# class Prey(Animal):
#   def flee(self):
#     print(f"{self.name} is fleeing")

# class Preditor(Animal):
#   def hunt(self):
#     print(f"{self.name} is hunting.")

# class Rabbit(Prey):
#   pass

# class Hawk(Preditor):
#   pass

# class Fish(Prey, Preditor):
#   pass

# hawk=Hawk("Tony")
# rabbit=Rabbit("Peter")
# fish=Fish("Nemo")

# hawk.hunt()
# rabbit.flee()
# fish.hunt()
# fish.flee()

# hawk.sleep()