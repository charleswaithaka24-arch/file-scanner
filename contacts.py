contacts={}
def add():
  while True:
    print("To exit enter x")
    name=input("Name :")
    if name=="x":
      break
    else:
      cell=input("Number :")
      contacts[name]=cell
      print("Contact successfully added ✅")

def search():
  while True:
    print("To exit enter x")
    cont=input("Enter name or cell no. to search\n:")
    if cont=="x":
      break
    elif cont in contacts.keys():
      print(f"{cont}: {contacts[cont]}")
    elif cont in contacts.values():
      print(f"{cont}: {contacts[cont]}")
    else:
      print("Not found")

def view():
  for n in contacts:
   print(f"{n}: {contacts[n]}")

while True:
  print("...SELECT AN OPTION...")
  menu=input("(1) Add a contact\n(2) Search a contact\n(3) View contacts\n(4) Exit\nChoose one :")
  if menu=="1":
    add()
  elif menu=="2":
    search()
  elif menu=="3":
    view()
  elif menu=="4":
    print("/..leaving page../")
    break