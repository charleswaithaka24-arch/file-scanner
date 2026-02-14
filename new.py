import json
with open("new_1.json","r") as v:
  content=json.load(v)
i=0
info=[]
for i in range(len(content)):
  info.append((content[i]['username'],content[i]['password']))
  i+=1


for e in range(3):
  user=input("Write your username :")
  pin=input("Write your password :")
  Entry=(user,pin)
   
  if Entry in info:
    print(f"Welcome {user}")
    break
  else :
    print("Incorrect password")
else :
  print("system locked")