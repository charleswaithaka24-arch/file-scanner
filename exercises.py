#try:
 #length=input("Enter square dimensions:")
 #side=int(length)
 #def area():
  #return(side*side)
 #print("The area is:",area())
#except ValueError:
 # print("incorrect_input.please enter again")
  #unit=input("Enter square dimensions:")
  #new=int(unit)
  #def rep():
   # return(new*new)
  #print("The area is:",rep())

#file_path=r'C:\Users\user\Desktop\javascript code\rock,paper,scissors.html'
#with open(r'C:\Users\user\Desktop\javascript code\rock,paper,scissors.html','r', encoding='UTF-8') as f:
 # content=f.read()
 # print(content)

#from pathlib import Path
#file_path=r"C:\Users\user\Desktop\javascript code\rock,paper,scissors.html"

from pathlib import Path
from collections import defaultdict
direction = Path("C:/Users/user/desktop")
contain = defaultdict(list)
total=sum(1 for folder in direction.iterdir() )
for file in direction.iterdir():
 if file.is_file():
   stats=file.stat()
   file_size=(f"{stats.st_size} bytes")
   ext = file.suffix
   contain[ext].append({f"{file.name}:{file_size}"})
for e, n in contain.items():
  print(e)
  print(" ",n)
sTats=direction.stat()
size=sTats.st_size
print(f"{direction.name} has these number of files and directories:",total)
print(f"Total size of authorised {direction.name} files and directories:",size,"bytes")