inventory={}
def product():
  while True:
    product=input("Enter product,enter 'x' to Exit :")
    if product=='x':
      break
    elif product in inventory.keys():
      print("Product already exists")
    else:
      price=float(input("Enter price :"))
      quantity=float(input("Enter quantity :"))
      inventory[product]={}
      inventory[product]["price"]=price
      inventory[product]["quantity"]=quantity

def price():
  while True:
    print("Enter x to exit")
    good=input("Enter product to update price :")
    if good=="x":
      break
    else:
      new_price=float(input("Enter new price :"))
      inventory[good]["price"]=new_price
      print("Price successfully updated ✅")
      print(inventory[good])

def quantity():
  while True:
    print("Enter x to exit")
    good=input("Enter product to update price :")
    if good=="x":
      break
    else:
      new_quantity=float(input("Enter new quantity :"))
      inventory[good]["quantity"]=new_quantity
      print("quantity successfully updated ✅")
      print(inventory[good])

def remove():
  while True:
    print("Enter x to exit")
    good=input("Enter name of product to remove :")
    if good=="x":
      break
    else:
      inventory.pop(good)
      print("Product successfully removed ✅")

def view():
  print(inventory)

while True:
  print("...WELCOME please select an option...")
  menu=input("(1) Add a product\n(2) Update price\n(3) Update quantity\n(4) Remove a product\n(5) View all products\n(6) Exit\nChoose any :")
  if menu=="1":
    product()
  elif menu=="2":
    price()
  elif menu=="3":
    quantity()
  elif menu=="4":
    remove()
  elif menu=="5":
    view()
  elif menu=="6":
    break