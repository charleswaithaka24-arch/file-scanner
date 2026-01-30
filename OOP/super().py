class Shape:
  def __init__(self,colour,is_filled):
    self.colour=colour
    self.is_filled=is_filled

class circle(Shape):
  def __init__(self,colour,is_filled,radius):
    super().__init__(colour,is_filled)
    self.radius=radius

class squire(Shape):
  def __init__(self,side):
    self.side=side

class triangle(Shape):
  def __init__(self,height,base):
    self.height=height
    self.base=base

Circle=circle("Blue",True,4)

print(Circle.colour)