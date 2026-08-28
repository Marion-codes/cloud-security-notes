print("Welcome to the Login System")

# Dictionary of users and their passwords that are already stored in the system.
users = {
    "admin": "1234"
}

failed_attempts = {}

locked_accounts = []

while True:
    # Asking the user if they want to login or create an account
    choice = input("Type login or create, or exit: ")

    if choice == "create":
        new_username = input("Create username: ")
    # Check if the username already exists in the users dictionary
        if new_username in users:
            print("Username already exists")

        else:
            new_password = input("Create password: ")
    # Add the new username and password to the users dictionary
            users[new_username] = new_password

            failed_attempts[new_username] = 0
            
            print("Account created successfully")
    
    elif choice == "login":
        
        username = input("Enter username: ")
        password = input("Enter password: ")

    # Check if the username is in the locked accounts list
        if username in locked_accounts:
            print("This acccount is locked")

    # Check if the username is in the users dictionary and if the password matches
        if username in users and users[username] == password:
            
            print("Login succcessful")

            failed_attempts[username] = 0
            
        else:
            print("Invalid login")
    # Check if the username is in the failed attempts dictionary, if not add it with a value of 0
            if username not in failed_attempts:
                failed_attempts[username] = 0

            failed_attempts[username] += 1

            print("Attempts:", failed_attempts[username])

    # if failed attempts for the username is greater than or equal to 3 
    # add the username to the locked accounts list and print out a message
            if failed_attempts[username] >= 3:

                locked_accounts.append(username)

                print("Account locked due to too many failed attempts")

    # If the username is not in the users dictionary then print out a message
            elif username not in users:
                print("Username does not exist")

    # Program closes if the user types "exit" and prints "Goodbye!"
    elif choice == "exit":
        print("Goodbye!")
        break

    # If user types anything other than login, create, or exit
    # then print out an error message
    else:
        print("Invalid option")

          
                
