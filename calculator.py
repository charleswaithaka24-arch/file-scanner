value = input("write your operation:")
try :
  calc = eval(value)
  print(calc)
except ZeroDivisionError :
  print('Undefined')
except (ValueError,TypeError,NameError) :
  print('incorrect input')
except OverflowError:
  print('Your value is too large')