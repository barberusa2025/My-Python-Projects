# point = {"x": 1, "y": 2} this is one way to create a dictionary

point = dict(x=1, y=2)  # This is another way to create a dictionary

print(point)

print(point["x"])  # Accessing the value associated with the key "x"
print(point["y"])  # Accessing the value associated with the key "y"


point["z"] = 3  # Adding a new key-value pair to the dictionary

if "a" in point:  # Checking if the key "a" exists in the dictionary
    print(point["a"])

del point["x"]  # Deleting the key "x" from the dictionary
print(point)

for key in point:  # Iterating over the keys in the dictionary
    print(key, point[key])  # Printing each key and its associated value
