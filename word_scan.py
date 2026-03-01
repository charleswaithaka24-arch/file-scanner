h=input("Write down a sentence\n:")
p=h.split()
r={}
q=[]
for a in p:
  if a in r:
    r[a]+=1
  else:
   r[a]=1
for y in r:
  q.append((y,r[y]))
order=sorted(q,key=lambda x:x[1],reverse=True)
print(order)
print(order[:1])