def error_control():
    try:
        n = int(input("Enter a number: "))
        print("Number:", n)
    except ValueError:
        print("Error, you must enter a number")

error_control()
