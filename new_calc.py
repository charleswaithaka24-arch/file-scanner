# Simple command-line calculator
def calculate():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+': print(num1 + num2)
        elif operator == '-': print(num1 - num2)
        elif operator == '*': print(num1 * num2)
        elif operator == '/':
            print(num1 / num2 if num2 != 0 else "Error: Division by zero")
        else: print("Invalid operator")
    except ValueError:
        print("Invalid input: Please enter numbers")

calculate() # Uncomment to run
