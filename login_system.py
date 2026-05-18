print("Welcome to the Login System")

users = {
    "admin": "1234"
}

failed_attempts = {}

locked_accounts = []

while True:

    choice = input("Type login or create, or exit: ")

    if choice == "create":
        new_username = input("Create username: ")
    
        if new_username in users:
            print("Username already exists")

        else:
            new_password = input("Create password: ")

            users[new_username] = new_password

            failed_attempts[new_username] = 0
            
            print("Account created successfully")
    
    elif choice == "login":
        
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in locked_accounts:
            print("This acccount is locked")

        if username in users and users[username] == password:
            
            print("Login succcessful")

            failed_attempts[username] = 0
            
        else:
            print("Invalid login")

            if username not in failed_attempts:
                failed_attempts[username] = 0

            failed_attempts[username] += 1

            print("Attempts:", failed_attempts[username])

            if failed_attempts[username] >= 3:

                locked_accounts.append(username)

                print("Account locked due to too many failed attempts")
            
    elif choice == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid option")

          
                
