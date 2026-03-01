class employee:
  def __init__(self,name):
    self.name=name
    self.salary=80000
  def annual(self):
    total_salary=self.salary*12
    return total_salary

class manager(employee):
  def __init__(self,name):
    super().__init__(name)
    self.bonus=20000
  def annual(self):
    pay=(self.salary+self.bonus)*12
    return pay
  
a_1=manager("Mike")
a_2=manager("Charles")
a_3=manager("James")
a_4=manager("Lucy")
a_5=employee("Regina")
a_6=employee("Collins")
a_7=employee("Grace")
a_8=employee("Alvin")
a_9=employee("Peter")
a_10=employee("Silas")
a_11=employee("Leonardo")
a_12=employee("Bob")
a_13=employee("April")


Workers=[a_1,a_2,a_3,a_4,a_5,a_6,a_7,a_8,a_9,a_10,a_11,a_12,a_13]

for worker in Workers:
 print(worker.name,worker.annual())