# Polymorphism having many forms
class Shape:

  def description(self):
    print(f"This is a shape.")

class circle(Shape):
  def __init__(self,radius):
    self.radius=radius

class square(Shape):
  def __init__(self,side):
    self.side=side

class triangle(Shape):
  def __init__(self,height,base):
    self.height=height
    self.base=base

class rock():
  def __init__(self,length,width):
    self.length=length
    self.width=width

  def description(self):
    print("This is a rock.")

shapes=[circle(4),square(4),triangle(4,5),rock(6,7)]
for shape in shapes:
  shape.description()

# Polymorphism through duck typing

class Dog:
  def speak(self):
    print("WOOF!")

class Cat:
  def speak(self):
    print("MEAOW!")

class Duck:
  def speak(self):
    print("QUACK!")

class Car:
  def speak(self):
    print("HONK!")

Animals=[Dog(),Cat(),Duck(),Car()]

for animal in Animals:
  animal.speak()