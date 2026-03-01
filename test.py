# try:
#          from pathlib import Path
#          from collections import defaultdict
#          direction=Path(input("input file path:"))
#          files_by_ext=defaultdict(list)
#          for current in direction.iterdir():
#             if current.is_file():
#                ext=current.suffix
#                stats=current.stat()
#                size =stats.st_size
#                files_by_ext[ext].append((current.name,size))
#               # print(current.name,size)
#          print()
#          print("Files by their extensions")
#          for e, n in files_by_ext.items():
#             print(e,)
#             print(" ",n )
#          total=sum(1 for folder in direction.iterdir() )
#          print()
#          print("TOTAL FILE SUMMARY")
#          for ext,files in files_by_ext.items():
#           largest_file=sorted(files,key=lambda x:x[1],reverse=True)
#           top=largest_file[:5]
#           print()
#           print(ext)
#           print("Largest files in each extension :",top)
#          print("Total number of files :",total)

#          print("Total file size :",direction.stat().st_size,"bytes")
         
# except FileNotFoundError:
#     print("Invalid file path")
# import json
# m={}
# a={}
# q=[]
# t={}
# m[5]=[]
# m[6]=[]
# #m.update(1)=7
# p=0
# x=1
# for y in range(20):
#  m[5].append(x)
#  p+=x
#  x+=1
# a[5]=p
# c=21
# d=0
# for l in range(20):
#  m[6].append(c)
#  d+=c
#  c+=1
# a[6]=d
# for v in a:
#  q.append((v,a[v]))

# for r in m:
#  for z in m[r]:
#   print(r)

# order=sorted(q,key=lambda x:x[1],reverse=True)
# for x in order:
#  t[x[0]]=x[1]
# for e in t:
#  print(f"{e}:{t[e]}")

# h="If cantie can tie a tie why can't I tie a tie"
# p=h.split()
# r={}
# for a in p:
#   if a in r.keys():
#     r[a]+=1
#   else:
#    r[a]=1
# print(r)

n={}
n["p"]=0
n["p"]+=1
print(n)