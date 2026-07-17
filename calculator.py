"""
Simple Calculator
-----------------

A command-line calculator built using Python that performs
basic arithmetic operations through an interactive menu.

Author: SARANSH ROUL

"""
from datetime import datetime


class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, num1, operator, num2):
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else None,
            "%": lambda a, b: a % b if b != 0 else None,
            "**": lambda a, b: a ** b,
        }

        if operator not in operations:
            return "Invalid operator."

        result = operations[operator](num1, num2)

        if result is None:
            return "Error: Division or modulus by zero."

        self.history.append(
            f"{datetime.now().strftime('%H:%M:%S')} | {num1} {operator} {num2} = {result}"
        )
        return result

    def show_history(self):
        if not self.history:
            print("\nNo calculations performed yet.\n")
            return

        print("\n Calculation History ")
        for item in self.history:
            print(item)
        print("Complete Calculation\n")

    def clear_history(self):
        self.history.clear()
        print("\nHistory cleared successfully.\n")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def menu():
    print( "_"* 45)
    print("         PYTHON CLI CALCULATOR")
    print( "_"* 45)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. View History")
    print("8. Clear History")
    print("9. Exit")
    print( "_"* 45)


def main():
    calculator = Calculator()

    operators = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "%",
        "6": "**",
    }

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "9":
            print("\nThank you for using the calculator!")
            break

        elif choice == "7":
            calculator.show_history()

        elif choice == "8":
            calculator.clear_history()

        elif choice in operators:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            result = calculator.calculate(num1, operators[choice], num2)

            print(f"\nResult: {result}\n")

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()