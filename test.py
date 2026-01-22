from pathlib import Path
from collections import defaultdict
direction=Path("C:/Users/user/Desktop/python_files")
files_by_ext=defaultdict(list)
for current in direction.iterdir():
 if current.is_file():
  ext=current.suffix
  stats=current.stat()
  size=stats.st_size
  files_by_ext[ext].append(current.name)
  files_by_ext[ext].append(f"{size} bytes")
  print(current.name,size)
for e, n in files_by_ext.items():
   print(e," ", n)
total=sum(1 for folder in direction.iterdir() )
print("Total number of files :",total)
print("Total file size :",direction.stat().st_size,"bytes")
largest_file=sorted(direction.stat().st_size,key=lambda f:f["size"])
top_5=largest_file[:5]
for top in top_5:
 print(top)