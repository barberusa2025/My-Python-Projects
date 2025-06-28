try:
    file = open("cleaning_up.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid input.")
else:
    print("No exceptions occurred.")

# This will close a file with or without an exception
finally:
    file.close()

