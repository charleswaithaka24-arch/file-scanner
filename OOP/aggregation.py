# an independent class references another independent classes
class Charles:
  class Garage:
    def __init__(self,name):
      self.name=name
      self.cars=[]

    def park(self,vehicle):
      self.cars.append(vehicle)
      
    def parked(self):
      return [f"{car.colour} {car.make} {car.model}" for car in self.cars]


  class Machine:
    def __init__(self,make,model,colour):
      self.make=make
      self.model=model
      self.colour=colour

  garage=Garage("Parkland")

  car_1=Machine("Ferrari","Roma Spider","Black")
  car_2=Machine("Lamborghini","Urus","Blue")
  car_3=Machine("Rolls Royce","Spectre","Dark Emarald")
  car_4=Machine("BMW","X6 M","Imperial Jade")



  garage.park(car_1)
  garage.park(car_2)
  garage.park(car_3)
  garage.park(car_4)

  for ride in garage.parked():
   print(f"\n{ride}")