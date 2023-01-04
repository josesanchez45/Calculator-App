import art

#add function
def add(n1, n2):
    return n1 + n2
#subtract function
def subtract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1/n2    


print(art.logo)








def calculator():
    more_calculations = False
    operations = {
    "+" : add, 
    "-":subtract,
    "*": multiply,
    "/": divide,  
    }
    num1 = float(input("What is the first number?:  "))

    for symbol in operations:
        print(symbol)

    while not more_calculations:
        operation_symbol = input("What is the operation?:  ")

        num2 = float(input("What is the next number?: "))

        calculation_function = operations[operation_symbol]

        answer= calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type y to continue calculations with {answer}? Enter y to continue or n to start over: ").lower() == "y":
            num1 = answer
        else:
            more_calculations = True
            calculator()

calculator()