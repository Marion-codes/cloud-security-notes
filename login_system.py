print("Welcome to the Login System")
correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Access denied. Attemps left:", attempts)

if attempts == 0:
        print("Account locked")
          
                
