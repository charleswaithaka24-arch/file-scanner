# Super() is used to inherit the parent's instance variables or methods.

class Shape:
  def __init__(self,colour,is_filled):
    self.colour=colour
    self.is_filled=is_filled

  def description(self):
    print(f"This is a {self.colour} shape. it is {"filled" if self.is_filled==True else "not filled"}.")

class circle(Shape):
  def __init__(self,colour,is_filled,radius):
    super().__init__(colour,is_filled)
    self.radius=radius

class square(Shape):
  def __init__(self,colour,is_filled,side):
    super().__init__(colour,is_filled)
    self.side=side

class triangle(Shape):
  def __init__(self,height,base):
    self.height=height
    self.base=base

Circle=circle("Blue",True,4)
Squire=square("yellow",True,3)

Squire.description()