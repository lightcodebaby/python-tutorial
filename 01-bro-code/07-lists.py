# List basics

food = ["pizza", "hamburger", "pasta"]

print(food)
print(food[0]) # pizza

food[0] = "bbq pizza"

print(food[0]) # bbq pizza

for x in food:
	print(x)

# List utils

food.append("ice cream")
food.remove("hamburger")
food.pop() # Remove the last element
food.inser(0, "cake")
food.sort() # alphabetically
food.clear()

# 2D lists = list of lists

drinks = ["monster", "reign", "zero coke"]
dinner = ["pizza", "hamburger", "salad"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

