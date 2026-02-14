# Composition is whereby a class directly owns another class or other classes in a way that they don't exist on their own

class Button:
  def __init__(self,num):
    self.num=num

class Screen:
  def __init__(self,size):
    self.size=size

class Calculator:
  def __init__(self,make,colour,buttons,screen):
    self.make=make
    self.colour=colour
    self.buttons=Button(buttons)
    self.screen=Screen(screen)

  def specs(self):
    return f"{self.make} {self.colour} {self.buttons.num}(buttons) {self.screen.size}(screen size)"

calc_1=Calculator("Casio","Black",45,"Medium")
calc_2=Calculator("basio","White",45,"Large")
calc_3=Calculator("radio","Grey",45,"Small")

Bag=[calc_1,calc_2,calc_3]
for item in Bag:
 print(item.specs())



