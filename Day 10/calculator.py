# Calculator

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

number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

for operation in operations:
    print(operation)
operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_symbol]
first_answer = calculation_function(number1, number2)
print(f"{number1} {operation_symbol} {number2} = {first_answer}")

number3 = int(input("Enter another number: "))
operation_symbol = input("Pick an operation from the line above: ")
second_answer = calculation_function(calculation_function(number1, number2), number3)
print(f"{first_answer} {operation_symbol} {number3} = {second_answer}")