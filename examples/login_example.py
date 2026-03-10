user = str(input("Enter user: "))
password = str(input("Enter password: "))

if user == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")