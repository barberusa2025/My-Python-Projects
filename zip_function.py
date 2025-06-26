list1 = [1, 2, 3]
list2 = [10, 20, 30]

# This will return an iterator of tuples
zip(list1, list2)

# To convert it to a list, we can use the list() function
print(list(zip(list1, list2)))
