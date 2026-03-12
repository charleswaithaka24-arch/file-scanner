# compound intrest calculator
def calculate_compound_interest(principal, annual_rate, years, compounds_per_year=1):
    amount = principal * ((1 + annual_rate / compounds_per_year) ** (compounds_per_year * years))
    return amount
while True:
  try:
    principal_amount = float(input("Enter the principal :"))
    interest_rate = float(input("Enter the rate :"))/100
    time_period_years = float(input("Enter the time in years :"))
    compounding_frequency = float(input("Enter number of times to compound per year,i.e, 4 for quartaly, 2 for half yearly or 1 for annually\n :"))

  except ValueError:
      print("Error: Please enter valid numeric values.")
  except ZeroDivisionError:
      print("Error: Cannot divide by zero!")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
  else:
     break
future_value = calculate_compound_interest(principal_amount, interest_rate, time_period_years, compounding_frequency)
compound_interest_earned = future_value - principal_amount
print("_"*80)
print(f"The future value after {time_period_years} years is: ${future_value:.2f}")
print(f"The compound interest earned is: ${compound_interest_earned:.2f}")
print("_"*80)