def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calculation = True
while calculation:
    num1 = float(input("Type the first number : "))

    operation = input("Pick an operation (+, -, *, /): ")

    num2 = float(input("Type the second number : "))


    if operation in operations:
        calculation_function = operations[operation]
        result = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
 
    
    next_calculation = True
    while next_calculation:
        print("want to continue calculating with the result? ")
        should_continue = input("Type 'yes' to continue or 'no' to new number first: ").lower()
        if should_continue == "yes":
            num1 = result
            operation = input("Pick an operation (+, -, *, /): ")
            num2 = float(input("Type the next number : "))
            if operation in operations:
                calculation_function = operations[operation]
                result = calculation_function(num1, num2)
                print(f"{num1} {operation} {num2} = {result}")
        else:
            next_calculation = False

    






# add_result = add(5, 7)
# print(f"The result of addition is: {add_result}")