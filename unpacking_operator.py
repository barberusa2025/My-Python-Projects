numbers = [1, 2, 3]
print(*numbers)  # Unpacking operator

values = [*range(5), *"Hello"]  # Unpacking operator with range and string
print(values)  # Output: [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']


first = {"x": 1}
second = {"x": 10, "y": 20}
combined = {**first, **second}  # Unpacking operator for dictionaries
print(combined)  # Output: {'x': 10, 'y': 20}
