items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product2", 9)
]

# Extracting prices from items
prices = [item[1] for item in items]
print(prices)

# Filtering prices less than 10
filtered_prices = [price for price in prices if price < 10]
print(filtered_prices)
