print("Welcome to the Login System")

users = {
    "admin": "1234"
}

choice = input("Type login or create account: ")

if choice == "create":
    new_username = input("Create username: ")
    
    if new_username in users:
        print("Username already exists")

    else:
        new_password = input("Create password: ")

        users[new_username] = new_password

        print("Account created successfully")
    
elif choice == "login":
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login succcessful")
    else:
        print("Invalid login")

elif choice == "exit":
    print("Goodbye!")
        
else:
    print("Invalid option")
          
                
