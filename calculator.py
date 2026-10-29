# calculator.py

def calculator():
    """A simple command-line calculator."""
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ").strip()
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
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    calculator()
