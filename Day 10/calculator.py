# Calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

# Add
def add(num1, num2):
    return num1 + num2

# Substract
def substract(num1, num2):
    return num1 - num2

# Multiply
def multiply(num1, num2):
    return num1 * num2

# Divide
def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    number1 = float(input("Enter your first number: "))

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        number2 = float(input("Enter your another number: "))
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {first_answer}")


        if input(f"Type 'y' to continue with the {first_answer} or 'n' to exit- ") == "y":
            number1 = first_answer
        else:
            should_continue = False
            calculator()
calculator()