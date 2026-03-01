import json
with open("new_1.json","r") as v:
  content=json.load(v)
i=0
info=[]
for i in range(len(content)):
  info.append((content[i]['username'],content[i]['password']))
  i+=1

def log_in():
  chances=4
  for e in range(3):
    chances-=1
    print(f"You have {chances} {"attempts" if chances>1 else "attempt"} left.")
    user=input("Write your username :")
    pin=input("Write your password :")
    Entry=(user,pin)
    if Entry in info:
      print(f"Welcome {user}")
      break
    else :
      print("⚠️"" "" User not found")
  else :
    print("system locked")

def sign_in():
  user=input("Write your new username :")
  pin=input("Write your new password :")
  print(f"Welcome {user}.")
  Entry={"username":user,"password":pin}
  content.append(Entry)
  
  with open("new_1.json","w") as d:
    json.dump(content,d)
while True:
  print("Enter 1, 2 or 3")
  Choice=input("(1) Log_in\n(2) Sign_in\n(3) Exit :")
  if Choice=="1":
    log_in()
    break
  elif Choice=="2":
    sign_in()
    break
  elif Choice=="3":
    print("Thank you for using our services.")
    break
  else :
    print("Invalid input\nPlease repeat")
    