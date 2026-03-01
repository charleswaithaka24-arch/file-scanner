import time
watch={}
print("SET TIMER")
Hours=int(input("Hours :"))
minutes=int(input("Minutes :"))
seconds=int(input("Seconds :"))
period=(Hours*3600)+(minutes*60)+seconds
for x in range(period):
  sec=x%60
  min=int(x/60)%60
  hour=int(x/3600)%24
  watch["time"]={f"{hour:02} : {min:02}: {sec:02}"}
  time.sleep(1)
  print(watch["time"])
print("Time's up!!")