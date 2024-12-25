# First create an add function
def add(num1, num2):
    return num1 + num2

# Second create a subtract function
def subtract(num1, num2):
    return num1 - num2

# Third create a multiply function
def multiply(num1, num2):
    return num1 * num2

# Fourth create a divided function
def divide(num1, num2):
    return num1 // num2

# Create a dictionary
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Create a calculate function
def calculate():
    try:
        number1 = int(input("Enter your first number: "))
        # for loop for showing symbols
        for operations in operators:
            print(operations)
        symbol = input("Pick an operations: ")
        number2 = int(input("Enter your second number: "))

        if symbol in operators:
            operation = operators[symbol]
            result = operation(number1, number2)
            print(f"Your result is: {number1} {symbol} {number2} = {result}.")
        else:
            print("Invalid operation symbol! Please choose from +, -, *, /.")
    except ValueError:
        print("Please enter a valid number or symbol!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculate()