import math

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'gcd' for Greatest Common Divisor")
    print("Enter 'square' for square of a number")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result:", result)git statu
    elif user_input == "subtract":
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        result = num1 - num2
        print("Result:", result)
    elif user_input == "multiply":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result:", result)
    elif user_input == "divide":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero")
    elif user_input == "gcd":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = math.gcd(num1, num2)
        print("GCD:", result)
    elif user_input == "square":
        num = float(input("Enter a number: "))
        result = num ** 2
        print("Square:", result)
    else:
        print("Wrong input, please enter one of 'add', 'subtract', 'multiply', 'divide', 'gcd', 'square', or 'quit'")
