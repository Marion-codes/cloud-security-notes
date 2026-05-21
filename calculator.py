# Simple Calculator v1

while True:
    num1= input("Enter first number (or type exit): ")

    if num1 == "exit":
        print("Goodbye!")
        break

    num2 = input("Enter second number: ")
    
    operation = input ("Choose +, -, *, / : ")

    if operation == "+":
        print(float(num1) + float(num2))
    
    elif operation == "-":
        print(float(num1) - float(num2))
        
    elif operation == "*":
        print(float(num1) * float(num2))
        
    elif operation == "/":
        if float(num2) == 0:
            print("Error: Cannot divide by zero")
        else:
            print(float(num1) / float(num2))
        
else:
    print("Invalid operation")
