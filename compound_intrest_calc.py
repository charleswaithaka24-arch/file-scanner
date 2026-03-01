def compound_I(principle,rate,time):
  return print(principle*((1+rate)**time))
def intrest(principle,rate,time):
  amount=principle*((1+rate)**time)
  intrest=amount-principle
  return print(intrest)
while True:
  try:
    principle=float(input("Enter the principle :"))
    rate=float(input("Enter the rate :"))/100
    time=float(input("Enter time in years :"))
    if principle<=0:
      print("Enter a valid principle")
    elif rate<0:
      print("Enter a valid rate")
    elif time<0:
      print("Enter a valid time")
    else :
      print("\nThe total amount is :")
      compound_I(principle,rate,time)
      print("\nThe total intrest is :")
      intrest(principle,rate,time)
      break
  except ValueError:
    print("Invalid input")