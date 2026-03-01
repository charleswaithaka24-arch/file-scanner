import random
n=float(input("Enter value to factorise :"))
def factorise(devidend):
  while True:
    divisor=random.randint(1,9)
    rem=devidend % divisor
    if rem==0 and divisor!=1 :
      quotient=devidend/divisor
      print(f"{devidend} : {divisor}\n{quotient}")
      return quotient
    
while True:
  n=factorise(n)
  if n==1:
    break
  elif n!=1:
    print("Prime number")
    break

