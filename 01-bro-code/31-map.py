store = [("shirt", 20.00), ("pants", 25.00), ("jacket", 50.00), ("socks", 10.00)]

discount = 0.8

apply_discount = lambda data: (data[0], data[1] * discount)

store_prices = list(map(apply_discount, store))

for item in store_prices:
    print(store)
