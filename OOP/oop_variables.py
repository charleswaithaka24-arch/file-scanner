# Instance variables and Class variables

class Student:

  class_year=2025# class variables
  num_students=0

  def __init__(self,name,age):
    self.name=name
    self.age=age
    Student.num_students+=1

student_1=Student("Spongebob",23)# instance variables
student_2=Student("Patrick",25)
student_3=Student("Sandy",22)

print(f"{student_1.name} is {student_1.age} years old.")
print(Student.class_year)
print(f"The graduating class of {Student.class_year} had {Student.num_students} students.")
print(student_1.name)
print(student_2.name)
print(student_3.name)