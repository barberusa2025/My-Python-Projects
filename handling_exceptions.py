try:
    age = int(input("Age:"))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
else:
    print("No exceptions were raised.")
