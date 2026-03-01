import time
start=time.time()
i=int(input("Enter value to find factorial :"))
ans=1
for v in range(i):
  ans*=i
  i-=1
fin=time.time()
period=fin-start
print(ans)
print(f"{period:.2f} seconds")