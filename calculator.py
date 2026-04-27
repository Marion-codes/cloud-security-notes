# Simple Calculator v1

Num1 = input ("Enter first number: ")
num2 = input ("Enter second number: ")

result = float(num1) + float(num2)

operation = input ("Choose +, -, *, /: ")

If operation == "+":
    print(num1 - num2)
elif operation == "-":
    print(num1 - num2) 
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid operation")
