
print("Welcome to Simple Calculator!")

while True:
    try:
        num1_input = input("Enter the first number (or 'q' to quit): ")

        if num1_input.lower() == "q":
            print("Goodbye!")
            break

        num1 = float(num1_input)
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
                continue
            result = num1 / num2
        else:
            print("Invalid operator. Please try again.")
            continue

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

