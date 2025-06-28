try:
# This will close the file automatically after use.
   with open("with_statement.py") as file:
    print("file opened.")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Invalid input.")
else:
    print("No exceptions occurred.")


