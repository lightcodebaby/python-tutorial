# A set is a collection which is unordered, unindexed and without duplciate values

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}


utensils.add("napkin")
utensils.remove("fork")

utensils.update(dishes)
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))  # fork, spoon
print(utensils.intersection(dishes))  # knife

for utensil in utensils:
    print(utensil)  # maybe in different order, only 1 knife


utensils.clear()
