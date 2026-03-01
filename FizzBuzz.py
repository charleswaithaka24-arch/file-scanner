def input_handling():
  while True:
  #range
   ran=int(input("Define a range,e.g. 1 :100\n1 :"))
   if ran<=1:
     print("Range should be more than 1")
   else:
     break
  #rules
  law={}
  g={}
  n=1
  k=[]
  o=[]
  t=[]
  f=[]
  while True:
    print("...TO FINISH ENTER 0...")
    while True:
      val=input("Enter a value to use :")
      if int(val)<0:
        print("Enter a positive integer")
      else:
        break
    if val=="0":
     break
    while True:
     id=input("Enter a word :")
     if id=="":
       print("Please enter a word")
     else:
      break
    value=int(val)
    n*=value
    law[value]=id
    g[value]=[]
    f.append(id)
    print(law)
    print(n)
  for i in range(ran):
    i+=1
    
    for l in law.keys():
      if i%(n)==0:
          k.append(i) 
      elif i%l==0:
        g[l].append(i)
    for h in g:
      for p in g[h]:
        t.append(p)
    if i not in t:
        o.append(i)

    if i in k:
      print(i,f)
    elif i in o:
      print(i,"")
    elif[i in h for h in g.values()]:
      for u in g.keys():
        if i%u==0:
          print(i,law.get(u))
input_handling()