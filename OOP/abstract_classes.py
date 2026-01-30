from abc import ABC, abstractmethod

class Vehicle(ABC):
  
  def __init__(self,name):
    self.name=name

  @abstractmethod
  def go(self):
    pass

  @abstractmethod
  def stop(self):
    pass

class Van(Vehicle):
  def go(self):
    print(f"This {self.name} is moving.")

  def stop(self):
    print(f"This {self.name} has stopped.")

class Boat(Vehicle):
  def go(self):
    print(f"This {self.name} is moving.")

  def stop(self):
    print(f"This {self.name} has stopped.")

class Jet(Vehicle):
  def go(self):
    print(f"This {self.name} is moving.")

  def stop(self):
    print(f"This {self.name} has stopped.")

van=Van("car")
boat=Boat("boat")
jet=Jet("jet")

van.stop()
boat.stop()
jet.stop()

van.go()
boat.go()
jet.go()