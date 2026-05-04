password = input("Enter a password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if len(password) < 8:
    print("Weak: Password should be at least 8 characters long")
elif password.islower() or password.isupper():
    print("Medium: Use both uppercase and lowercase letters")
elif password.isalnum():
    print("Medium: Add special characters (!, @, #, etc.)")
else:
     print("Your Password is Strong")

input("Press Enter to exit!")
