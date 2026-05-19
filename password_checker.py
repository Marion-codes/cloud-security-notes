while True:
    password = input("Enter a password (or type exit): ")
    if password == "exit":
        print("Goodbye!")
        break

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if len(password) < 8:
        print("Weak: Password should be at least 8 characters long")
    
    elif not has_upper or not has_lower:
        print("Medium: Use both uppercase and lowercase letters")

    elif not has_digit or not has_lower:
        print("Medium: Add numbers to your password")
    
    elif not has_special:
        print("Medium: Add special characters (!, @, #, etc.)")
    
    else:
        print("Your Password is Strong")

