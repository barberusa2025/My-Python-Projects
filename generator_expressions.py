from sys import getsizeof

# Generator expression
# This will create a generator object that yields values one at a time,
# which is memory efficient.
# It does not create a list in memory, so it consumes less memory.
# The generator will only compute the next value when requested.
# This is useful for large datasets or when you want to save memory.
# The generator expression is enclosed in parentheses.
# It is similar to a list comprehension but uses parentheses instead of square brackets.
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))


# List comprehension
# This will create a list in memory, which can be large
# and consume a lot of memory.
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
