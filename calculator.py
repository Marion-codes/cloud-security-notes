# Simple Calculator
# This program performs basic math operations 
# and allows the user to continue calculating until they type "exit"

while True:
    # Get the first number from the user
    num1= input("Enter first number (or type exit): ")

    # Exit the calculator if the user enters "exit"
    if num1 == "exit":
        print("Goodbye!")
        break

    # Ask the user for a second number
    num2 = input("Enter second number: ")

    # Ask the user which operation that they would like to use
    operation = input ("Choose +, -, *, /:")

    if operation == "+":
        print(float(num1) + float(num2))
    
    elif operation == "-":
        print(float(num1) - float(num2))
        
    elif operation == "*":
        print(float(num1) * float(num2))
        
    elif operation == "/":
        # If the second number is equal to 0 then print out a error message
        if float(num2) == 0:
            print("Error: Cannot divide by zero")
        # If not then skip to regular divison
        else:
            print(float(num1) / float(num2))
# If user doesnt give a number or operation then print out an error message
    else:
        print("Invalid operation")