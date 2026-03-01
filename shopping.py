class products:
  def __init__(self,name,price):
    self.name=name
    self.price=price

class cart:
  def __init__(self):
    self.items=[]

  def add(self,good):
    self.items.append(good)

  def rem(self,good):
    self.items.remove(good)
    print(f"Removed {good.name}\nRemaining products :")
    for item in self.items:
     print(f"{item.name}: {item.price}")


  def cost(self):
    total=0
    for item in self.items:
      total+=item.price
    return total

  def summary(self):
    for item in self.items:
     print(f"{item.name}: {item.price}")
    print(f"Total cost: {cart.cost(self)}")

v=cart()

a=products("sugar",200)
b=products("rice",300)
c=products("oil",400)
d=products("floor",1200)
e=products("juice",250)

v.add(a)
v.add(b)
v.add(c)
v.add(d)
v.add(e)

v.rem(c)