# Password Checker Program

while True:
    # Get a password from the user if password = exit then close program
    password = input("Enter a password (or type exit): ")
    if password == "exit":
        print("Goodbye!")
        break

    # Check if password has atleast one uppercase letter
    # lowercase letter, digit, and special character
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    # Check password length and if it has uppercase, 
    # lowercase, digit, and special character
    if len(password) < 8:
        print("Weak: Password should be at least 8 characters long")
    
    elif not has_upper or not has_lower:
        print("Medium: Use both uppercase and lowercase letters")

    elif not has_digit or not has_lower:
        print("Medium: Add numbers to your password")
    
    elif not has_special:
        print("Medium: Add special characters (!, @, #, etc.)")

    # If password meets all the requirements then print out a message
    else:
        print("Your Password is Strong")

