items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product2", 9)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
