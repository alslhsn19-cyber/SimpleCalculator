
print("Welcome to Simple Calculator!")

try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid operator.")

    if operator in ["+", "-", "*"]:
        print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")
