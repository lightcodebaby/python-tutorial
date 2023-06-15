cities_summer_temperatures = {
    "Madrid": 35,
    "Barcelona": 30,
    "Canarias": 25,
    "Talavera": 40,
}

cities_winter_temperatures = {
    key: (value - 15) for (key, value) in cities_summer_temperatures.items()
}

print(cities_winter_temperatures)

weather = {
    "Madrid": "snowing",
    "Barcelona": "cloudy",
    "Canarias": "sunny",
    "Talavera": "raining",
}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}

desc_cities = {
    key: ("WARM" if value > 30 else "COLD")
    for (key, value) in cities_summer_temperatures.items()
}

# or...


def check_temp(value):
    if value > 30:
        return "HOT"
    else:
        return "COLD"


desc_cities = {
    key: check_temp(value) for (key, value) in cities_summer_temperatures.items()
}
