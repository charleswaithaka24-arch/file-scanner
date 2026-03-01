record={}
averages={}
merit=[]
rank={}
def basic_info():
  while True:
    student=input("To finish enter 0\nStudent's name :")
    if student=="0":
      break
    else:
      record[student]=[]
      sub=int(input("Number of subjects :"))
      k=0
      while k<sub:
        grades=float(input("Student's grades :"))
        if grades<0 or grades >100:
          print("Invalid entry")
        else:
          record[student].append(grades)
          k+=1

def average():
  for h in record:
    a=0
    for y in record[h]:
      a+=y
    averages[h]=a/len(record[h])
  b=0
  for u in averages:
      b+=averages[u]
  rank["class mean"]=b/len(averages)

def order():
  for avg in averages:
    merit.append((avg,averages[avg]))
  ordered=sorted(merit,key=lambda x:x[1],reverse=True)
  for each in ordered:
    rank[each[0]]=each[1]
  print("...OVERALL PERFORMANCE...\n")
  pos=0
  for i in rank:
   print(f"{pos}. {i}:{rank[i]}")
   pos+=1

basic_info()
average()
order()