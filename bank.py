class bank:
  def __init__(self,name):
    self.name=name
    self.balance={}
    self.balance["Balance"]=0
    self.summary={}
    self.summary[self.name]=self.balance
    accounts=len(self.summary)
    accounts=accounts
  def get_balance(self):
    return print(self.balance)
  def deposit(self,amount):
    if amount<=0:
      print("Please enter a valid amount.")
    else:
     self.balance["Balance"]+=amount
  def withdraw(self,amount):
    if amount>self.balance["Balance"]:
      print("Inssuficient balance,please top up account in order to transact.")
    else:
     self.balance["Balance"]-=amount

individual_1=bank("Mike")
individual_2=bank("Charles")
individual_3=bank("James")
individual_4=bank("Lucy")
individual_5=bank("Regina")
individual_6=bank("Collins")
individual_7=bank("Grace")

individual_1.deposit(20000000)
individual_2.deposit(26000000)
individual_3.deposit(12000000)

individual_2.get_balance()

print(individual_2.summary)