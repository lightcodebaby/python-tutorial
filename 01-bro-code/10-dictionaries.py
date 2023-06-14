# A dictionary is a changeable, unordered collection of unique key:value pairs

capitals = {
    "USA": "Washington DC",
    "India": "New Dehli",
    "Spain": "Madrid",
    "China": "Beijing",
    "Russia": "Moscow",
}

print(capitals["Spain"])  # Madrid
print(capitals.get("Germany"))  # None
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({"Germany": "Berlin"})
capitals.update({"Spain": "Madriz"})

capitals.pop("China")  # Removes China

for key, value in capitals.items():
    print(key, value)
