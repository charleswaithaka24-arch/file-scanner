import random
attempts=0

def game(secret,num_attempts,attempts):
  while True:
    try:
      print(f"You have {num_attempts} remainig attempts.")
      guess=int(input("Guess a number :"))
      attempts+=1
      num_attempts-=1
      if num_attempts>0:
        if secret==guess:
          print("Correct!!")
          print(f"Number of attempts :{attempts}")
          break
        elif secret<guess:
          print("Too high")
        elif secret>guess:
          print("Too low")
      else :
        print("Game over.\nYou lost😂😂!!")
    except ValueError:
      print("Enter a number")

while True:
  print("...NUMBER GUESSING GAME...")
  print("Choose Level of difficulty")
  print("To exit enter '5'")
  diff=input("(1) Hard\n(2) Normal\n(3) Easy\nChoice :")
  if diff=="1":
    secret=random.randint(1,100)
    num_attempts=10
    game(secret,num_attempts,attempts)
    break
  elif diff=="2":
    secret=random.randint(1,50)
    num_attempts=15
    game(secret,num_attempts,attempts)
    break
  elif diff=="3":
    secret=random.randint(1,100)
    num_attempts=10
    game(secret,num_attempts,attempts)
    break
  elif diff=="5":
    break
  else:
    print("Invalid entry")